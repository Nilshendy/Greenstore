# GreenStore - Inventory Management System

## Project Overview

GreenStore is een geïntegreerd voorraad- en klantbeheersysteem voor een duurzaam retail bedrijf. Het systeem automatiseert voorraadbeheer, klantgegevens, en verkoopprocessen met geautomatiseerde rapportages.

## Projectdoel

Ontwikkeling van een softwareoplossing die:
- Automatisch voorraad en klantbeheer regelt
- Fouten in voorraadniveaus en vertragingen vermindert
- Lange verwerkingstijd van klantbestellingen optimaliseert
- Geautomatiseerde rapportages genereert over verkoopcijfers en klantactiviteit

## Tech Stack

### Backend Options

#### **Optie 1: Python (FastAPI) - AANBEVOLEN**
- **Waarom**: Beste voor data processing, rapportages, en business logic
- **Voordelen**: 
  - Snelle development met type hints
  - Automatische API documentatie (Swagger)
  - Excellent voor berekeningen en data analysis
  - Async support voor performance
- **Gebruik voor**: 
  - REST API endpoints
  - Voorraadberekeningen
  - Rapportage generatie
  - Database operaties

#### **Optie 2: PHP (Laravel/Pure PHP)**
- **Waarom**: Traditionele web development, breed ondersteund
- **Voordelen**:
  - Goedkope hosting opties
  - Grote community
  - Eenvoudige deployment
- **Gebruik voor**:
  - Formulier handling
  - Session management
  - Traditionele server-side rendering

### Frontend

#### **HTML5 + CSS3 (Tailwind CSS)**
- **Gebruik voor**: 
  - Structuur en layout
  - Responsive design
  - Modern UI components

#### **JavaScript (Vanilla ES6+)**
- **Gebruik voor**:
  - Dynamic UI updates
  - Client-side validatie
  - AJAX calls naar backend
  - Real-time voorraad updates
  - Interactive dashboards

### Database
- **SQLite** (Development) / **PostgreSQL** (Production)
- **Waarom**: Relationele data (producten, klanten, bestellingen)

## Project Structuur

```
GreenStore/
├── backend/
│   ├── python/                 # Python FastAPI implementatie
│   │   ├── app/
│   │   │   ├── main.py        # FastAPI application
│   │   │   ├── models.py      # Database models
│   │   │   ├── routes/        # API endpoints
│   │   │   ├── services/      # Business logic
│   │   │   └── utils/         # Helper functions
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   └── php/                    # PHP alternatieve implementatie
│       ├── api/
│       ├── config/
│       ├── models/
│       └── README.md
│
├── frontend/
│   ├── index.html             # Dashboard
│   ├── inventory.html         # Voorraad management
│   ├── customers.html         # Klantbeheer
│   ├── orders.html            # Bestellingen
│   ├── reports.html           # Rapportages
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── app.js             # Main application logic
│       ├── inventory.js       # Voorraad functionaliteit
│       ├── customers.js       # Klant management
│       └── api.js             # API communication
│
├── database/
│   ├── schema.sql             # Database schema
│   └── seed_data.sql          # Test data
│
├── docs/
│   ├── API_DOCUMENTATION.md
│   └── USER_GUIDE.md
│
└── README.md
```

## Features

### Core Functionaliteit

1. **Voorraad Management**
   - Real-time voorraad tracking
   - Automatische low-stock alerts
   - Product categorisatie
   - Voorraad geschiedenis

2. **Klantbeheer**
   - Klantprofielen
   - Bestelgeschiedenis
   - Klant segmentatie
   - Contact informatie

3. **Bestelling Processing**
   - Order creation en tracking
   - Automatische voorraad updates
   - Order status management
   - Leveringsplanning

4. **Rapportages**
   - Verkoopstatistieken
   - Voorraad rapporten
   - Klantactiviteit analyse
   - Export naar CSV/PDF

5. **Dashboard**
   - Real-time metrics
   - Visuele grafieken
   - Quick actions
   - Notificaties

## Installatie & Setup

### Python Backend (Aanbevolen)

```bash
# Navigeer naar backend directory
cd backend/python

# Maak virtual environment
python -m venv venv

# Activeer virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Installeer dependencies
pip install -r requirements.txt

# Run database migrations
python -m app.database.init_db

# Start de server
uvicorn app.main:app --reload --port 8000
```

### PHP Backend (Alternatief)

```bash
# Navigeer naar backend directory
cd backend/php

# Installeer dependencies (als je Composer gebruikt)
composer install

# Configureer database in config/database.php

# Start PHP development server
php -S localhost:8000
```

### Frontend

```bash
# Open frontend/index.html in browser
# Of gebruik een local server:
cd frontend
python -m http.server 3000
# Of met PHP:
php -S localhost:3000
```

## Database Schema

### Tabellen

- **products** - Product informatie en voorraad
- **customers** - Klantgegevens
- **orders** - Bestellingen
- **order_items** - Bestelling details
- **inventory_logs** - Voorraad mutaties
- **reports** - Gegenereerde rapporten

## API Endpoints

### Python (FastAPI)

```
GET    /api/products              - Alle producten
POST   /api/products              - Nieuw product
GET    /api/products/{id}         - Product details
PUT    /api/products/{id}         - Update product
DELETE /api/products/{id}         - Verwijder product

GET    /api/customers             - Alle klanten
POST   /api/customers             - Nieuwe klant
GET    /api/customers/{id}        - Klant details

GET    /api/orders                - Alle bestellingen
POST   /api/orders                - Nieuwe bestelling
GET    /api/orders/{id}           - Bestelling details

GET    /api/reports/sales         - Verkoop rapport
GET    /api/reports/inventory     - Voorraad rapport
GET    /api/reports/customers     - Klant activiteit
```

## UI/UX Features

- **Responsive Design** - Werkt op desktop, tablet, en mobile
- **Modern Interface** - Clean en intuïtief
- **Real-time Updates** - Live voorraad status
- **Dark Mode** - Oog-vriendelijke interface
- **Accessibility** - WCAG 2.1 compliant

## Testing

```bash
# Python backend tests
cd backend/python
pytest

# JavaScript frontend tests
cd frontend
npm test
```

## Toekomstige Uitbreidingen

- [ ] Barcode scanning
- [ ] Multi-warehouse support
- [ ] Email notificaties
- [ ] Mobile app (React Native)
- [ ] Advanced analytics met ML
- [ ] Integration met accounting software

## Team & Agile Workflow

- **Scrum Methodologie**: Sprints van 1-2 weken
- **GitLab Repository**: Versiebeheer en code reviews
- **Daily Stand-ups**: Voortgang tracking
- **Retrospectives**: Continue verbetering

## Deliverables

1.  Functioneel en technisch ontwerpdocument
2.  Werkende softwareoplossing (voorraad- en klantbeheer)
3.  GitLab repository met codeversies
4.  Test resultaten (unit, integratie, gebruikerstests)
5.  Eindrapport en evaluatie
6.  Individuele reflectie van studenten
7.  Eindpresentatie in het Engels

## Licentie

MIT License - Vrij te gebruiken voor educatieve doeleinden

## Contact

Voor vragen over het project, neem contact op met het development team.

---

Ontwikkeld voor: GreenStore Retail
Project Duur: 5 werkdagen (1 week)
Onderwerp: Software Development Project
**Project Duur**: 5 werkdagen (1 week)
**Onderwerp**: Software Development Project
