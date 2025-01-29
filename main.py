import os
from datetime import datetime

import pytz
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

# Load environment variables
load_dotenv()

MAX_NAME_LENGTH = 15
MAX_MESSAGE_LENGTH = 50
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %p %Z"

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

app, rt = fast_app(
        hdrs=(Link(rel="icon", type="assets/x-icon", href="/assets/favicon.png"),),
)

def get_est_time():
    est_tz = pytz.timezone("US/Eastern")
    return datetime.now(est_tz)

def add_message(name, message):
    timestamp = get_est_time().strftime(TIMESTAMP_FORMAT)
    supabase.table("MyGuestbook").insert(
        {"name": name, "message": message, "timestamp": timestamp}
    ).execute()

def get_messages():
    #sort by id in descending order to get the latest entries first
    response = (
        supabase.table("MyGuestbook").select("*").order("id", desc=True).execute()
    )
    return response.data

def render_message(entry):
    return(
        Article(
            Header(f"Name: {entry["name"]}"),
            P(entry["message"]),
            Footer(Small(I(f"Posted: {entry["timestamp"]}")),),
        )
    )

def render_message_list():
    messages = get_messages()
    
    return Div(
        *map(render_message, messages),
        id="message-list",
    )

def render_content():
    form = Form(
        Fieldset(
            Input(
                type="text",
                name="name", 
                placeholder="Name", 
                required=True, 
                maxlenght=MAX_NAME_LENGTH
            ),
            Input(type="text", 
                name="message", 
                placeholder="Message", 
                required=True, 
                maxlenght=MAX_MESSAGE_LENGTH
            ),
            Button("Submit", type="submit"),
            role="group",
        ),

        method="post",
        hx_post="/submit-message", # Send POST request to /submit-message endpoint
        hx_target="#message-list", # Update only the message list after submitting
        hx_swap="outerHTML", # Replace the entire content of the target element with the response
        hx_on__after_request="this.reset()", # Reset the form after submitting
    )

    return Div(
        P(I("Write something nice!")),
        form,
        Div(
            "Made with ❤️ by ",
            A("Benji", href="https://github.com/notSoEliel", target="_blank"),
        ),
        Hr(),
        P("Here are some nice messages:"),
        render_message_list(),
    )

@rt("/")
def get():
    return Titled("My Guestbook 📖", render_content())

@rt("/submit-message", methods=["POST"])
def post(name: str, message: str):
    add_message(name, message)
    return render_message_list()

serve()