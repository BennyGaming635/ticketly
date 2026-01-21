# Ticketly 🎫

A self-hosted ticket management platform built with Python, FastAPI, and PostgreSQL. Ticketly provides a complete solution for managing events, selling tickets, and handling orders.

## Features

- 🔐 **User Authentication**: Secure JWT-based authentication with HTTP-only cookies
- 👥 **User Accounts**: Email and password-based account creation and management
- 🎉 **Event Management**: Create and manage events with multiple ticket types
- 🎟️ **Ticket Sales**: Support for various ticket types with pricing and availability
- 📦 **Order Processing**: Complete order management system
- 🔒 **Password Security**: Bcrypt password hashing for secure storage
- 🐳 **Docker Support**: Easy deployment with Docker and Docker Compose

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Bcrypt
- **Containerization**: Docker & Docker Compose

## Project Structure

```
ticketly/
├── app/
│   ├── auth/              # Authentication utilities and dependencies
│   ├── config/            # Configuration and database setup
│   ├── models/            # SQLAlchemy database models
│   ├── routes/            # API route handlers
│   ├── schemas/           # Pydantic schemas for validation
│   └── main.py            # FastAPI application entry point
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker image configuration
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
└── README.md              # This file
```

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Git (for cloning the repository)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BennyGaming635/ticketly.git
   cd ticketly
   ```

2. **Create environment file**:
   ```bash
   cp .env.example .env
   ```

3. **Update the `.env` file** with your configuration:
   ```env
   DATABASE_URL=postgresql://ticketly_user:ticketly_password@db:5432/ticketly_db
   SECRET_KEY=your-secret-key-here-change-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   APP_NAME=Ticketly
   DEBUG=True
   ```

   ⚠️ **Important**: Change the `SECRET_KEY` to a secure random string in production!

4. **Build and start the application**:
   ```bash
   docker-compose up --build
   ```

   The application will be available at:
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

5. **Stop the application**:
   ```bash
   docker-compose down
   ```

## API Endpoints

### Public Endpoints

- `GET /` - Welcome message and API information
- `GET /health` - Health check endpoint

### Authentication Endpoints

- `POST /auth/register` - Register a new user account
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- `POST /auth/login` - Login and receive JWT token
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- `POST /auth/logout` - Logout and clear authentication cookie

- `GET /auth/me` - Get current authenticated user information (requires authentication)

## Database Models

### User
- User accounts with email and hashed passwords
- Active status and admin privileges
- Timestamps for creation and updates

### Event
- Event details (title, description, location)
- Start and end datetime
- Maximum ticket capacity

### TicketType
- Different ticket types per event (e.g., General, VIP)
- Pricing and availability tracking
- Quantity management

### Order
- Purchase orders linked to users and events
- Order status tracking (pending, completed, cancelled, refunded)
- Total amount calculation

### Ticket
- Individual tickets with unique codes
- Check-in status tracking
- Linked to orders and ticket types

## Development

### Running without Docker

1. **Install Python 3.11+**

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL** and update the `DATABASE_URL` in `.env`

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

### Testing the API

You can test the API using the interactive documentation at http://localhost:8000/docs or use curl:

```bash
# Register a new user
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
```

## Security Considerations

- 🔐 Always use HTTPS in production
- 🔑 Change the `SECRET_KEY` to a strong, random value
- 🍪 Set `secure=True` for cookies when using HTTPS
- 🚫 Never commit `.env` files to version control
- 🔒 Use strong passwords and implement rate limiting
- 📝 Regularly update dependencies for security patches

## Future Enhancements

- Email verification for new accounts
- Password reset functionality
- Payment gateway integration
- QR code generation for tickets
- Event analytics and reporting
- Admin dashboard
- Mobile app support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on GitHub.