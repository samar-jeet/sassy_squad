Here’s an updated version of the README file with the **tech stack** section added:

---

# SassySquad

**SassySquad** is a group collaboration website that allows users to interact through video, audio, and text messaging. It includes functionality for file sharing, user management, and organizing content into folders. The platform is ideal for teams and communities looking to collaborate and communicate efficiently in a shared digital space.

## Features
- **Chat (Video/Audio/Text):** Users can engage in real-time communication with group members.
- **Media Sharing:** Upload and share files via drive links, with folder creation for better organization.
- **Memories:** A section to store and display shared group moments or important files.
- **User Profiles:** Each member's details and profile picture are displayed on the home screen for easy identification and access.
- **User Management:** Includes features for managing users and controlling access to files and communication.

## Project Structure

```
SassySquad/
│
├── chat/          # Chat functionalities for video, audio, and text
├── core/          # Core functionality and settings of the website
├── media/         # Folder to handle media file uploads and organization
├── memories/      # Section to store shared moments or important files
├── sassy/         # Main application files
├── users/         # User profiles and details management
│
├── db.sqlite3     # SQLite database file
├── manage.py      # Main management script for running the Django app
├── requirements.txt # List of project dependencies
```

## Tech Stack

- **Frontend:** 
  - HTML5
  - CSS3
  - JavaScript
  
- **Backend:** 
  - **Django** (Python framework)
  - **Django Channels** for real-time WebSocket connections (Video/Audio/Text chat)
  
- **Database:** 
  - **SQLite** (for local development)
  - [PostgreSQL or MySQL] (for production environment, if applicable)

- **Media Storage:**
  - Local storage or **AWS S3** for file uploads (optional)

- **WebSocket & Real-time Communication:** 
  - **Django Channels**
  - **Redis** (for handling WebSocket connections and real-time features)

- **Authentication:**
  - Django's built-in authentication system

- **Deployment:**
  - **Gunicorn** and **Nginx** for server management (for production)
  - **Docker** (optional, for containerization)

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/SassySquad.git
   cd SassySquad
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the project:**
   ```
   python manage.py migrate
   python manage.py runserver
   ```

4. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Chat:** Navigate to the chat section to initiate video/audio calls or send messages.
- **Media:** Upload and share files with group members, creating folders for organization.
- **User Profiles:** View and manage member details, including profile pictures.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project.
