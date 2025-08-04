"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
# Added 8 sports, 8 artistic, and 8 intellectual activities

activities = {
    # Sports activities
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball and play friendly games",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Tennis Club": {
        "description": "Learn and play tennis with peers",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Swimming Team": {
        "description": "Swim training and competitions",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Volleyball Club": {
        "description": "Practice volleyball and participate in tournaments",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": []
    },
    "Track and Field": {
        "description": "Join track and field events and improve your athletic skills",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },

    # Artistic activities
    "Art Club": {
        "description": "Explore painting, drawing, and sculpture",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Drama Club": {
        "description": "Act, direct, and produce school plays",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Choir": {
        "description": "Sing in the school choir and perform at events",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Photography Club": {
        "description": "Learn photography and participate in photo walks",
        "schedule": "Fridays, 4:00 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    "Dance Club": {
        "description": "Practice various dance styles and perform at school events",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Orchestra": {
        "description": "Play instruments and perform orchestral music",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 30,
        "participants": []
    },
    "Film Club": {
        "description": "Watch, discuss, and create short films",
        "schedule": "Mondays, 4:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Creative Writing": {
        "description": "Write stories, poems, and participate in writing contests",
        "schedule": "Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },

    # Intellectual activities
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and compete in math contests",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Debate Team": {
        "description": "Develop argumentation skills and compete in debates",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Robotics Club": {
        "description": "Build robots and participate in competitions",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": []
    },
    "Book Club": {
        "description": "Read and discuss books from various genres",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": []
    },
    "Quiz Bowl": {
        "description": "Compete in academic quiz competitions",
        "schedule": "Fridays, 4:00 PM - 5:00 PM",
        "max_participants": 8,
        "participants": []
    },
    "Language Club": {
        "description": "Learn new languages and explore different cultures",
        "schedule": "Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    }
}
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities

# Validate student is not already signed up
@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
