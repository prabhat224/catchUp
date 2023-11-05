# Problem Statement

Despite the prevalence of social media, relocating to new cities often leads to a loss of meaningful connections. CatchUp addresses this by prioritizing real-world interactions, notifying users about old friends. Our platform aims to rekindle and strengthen genuine connections, combating the isolation of relocation.

# Solution

A social media application designed for bringing together friends and community members who are separated by distance . After the the user sign up they can see the location of the friends who are in their area .

# Our PPT

Check the File named as catchUp.pptx in the repo

# Details

Catchup is a dynamic chat application built using the Taipy library in Python with a Django backend. It not only facilitates seamless communication but also integrates community meetups based on user location. Additionally, users can add new friends to their existing communities and extend invites to others.

## Features

- **Real-time Chat**: Engage in instant, real-time conversations with friends and community members.
- **Location-Based Meetups**: Discover and join local meetups organized by communities.
- **Add Friends**: Easily add new friends to your existing communities for enhanced social interaction.
- **Community Invitations**: Extend invitations to others, encouraging them to join your community.

## Setup Instructions

1. **Clone the Repository**

   ```
   git clone https://github.com/yourusername/catchup-chat.git
   cd catchup-chat
   ```

2. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Apply Migrations**

   ```
   python manage.py migrate
   ```

4. **Run the Server**

   ```
   python manage.py runserver
   ```

   The application will now be accessible at `http://localhost:8000`.

5. **Create a Superuser (Optional)**

   ```
   python manage.py createsuperuser
   ```

   This step is useful for accessing the Django admin interface.

## Usage

1. **Register and Log In**

   Create an account or log in if you already have one.

2. **Explore Communities**

   Browse existing communities and join ones that interest you.

3. **Add Friends**

   Add new friends to your existing communities for personalized interaction.

4. **Organize Meetups**

   Create and manage meetups based on your location for community members to join.

5. **Invite Others**

   Extend invites to friends and acquaintances to join your community and participate in activities.
