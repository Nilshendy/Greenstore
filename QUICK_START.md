# GreenStore Quick Start Guide

## Snelle Setup in 5 Minuten

### Optie 1: Automatische Setup (Aanbevolen)

#### Windows

```powershell
# 1. Navigeer naar project directory
cd C:\Users\Nilsh\CascadeProjects\GreenStore

# 2. Run setup script
python setup.py

# 3. Start backend
cd backend\python
uvicorn app.main:app --reload --port 8000

# 4. Start frontend (nieuwe terminal)
cd frontend
python -m http.server 3000

# 5. Open browser
# http://localhost:3000
```

#### Linux/Mac

```bash
# 1. Navigeer naar project directory
cd ~/CascadeProjects/GreenStore

# 2. Run setup script
python3 setup.py

# 3. Start backend
cd backend/python
uvicorn app.main:app --reload --port 8000

# 4. Start frontend (nieuwe terminal)
cd frontend
python3 -m http.server 3000

# 5. Open browser
# http://localhost:3000
```

---

### Optie 2: Handmatige Setup

#### Stap 1: Python Dependencies Installeren

```bash
cd backend/python
pip install -r requirements.txt
```

#### Stap 2: Database Initialiseren

```bash
python -c "from app.database import init_db, seed_database; init_db(); seed_database()"
```

#### Stap 3: Backend Starten

```bash
uvicorn app.main:app --reload --port 8000
```

#### Stap 4: Frontend Starten (nieuwe terminal)

```bash
cd frontend
python -m http.server 3000
```

---

### Optie 3: PHP Backend (Alternatief)

Als je liever PHP gebruikt:

```bash
# 1. Navigeer naar PHP backend
cd backend/php

# 2. Start PHP server
php -S localhost:8000

# 3. Start frontend (nieuwe terminal)
cd frontend
python -m http.server 3000
# Of met PHP:
php -S localhost:3000
```

---

## Toegang tot de Applicatie

### Login Pagina
```
http://localhost:3000/login.html
```

**Let op:** `login.html` opent standaard de **Klant Login**.

- Klant Login: `http://localhost:3000/shop/login.html`
- Werknemer Login: `http://localhost:3000/login.html?werknemer=1`

### Login Gegevens

| Rol | Email | Wachtwoord | Gaat naar |
|-----|-------|------------|-----------|
| Werknemer | `werknemer@gmail.com` | `wachtwoord` | Werknemer Dashboard |
| Manager | `manager@gmail.com` | `wachtwoord` | Manager Dashboard |
| Klant (voorbeeld) | `emma.devries@gmail.com` | `wachtwoord` | Klant Dashboard |
| Klant (voorbeeld) | `lucas.jansen@gmail.com` | `wachtwoord` | Klant Dashboard |

### Manager Dashboard
```
http://localhost:3000/manager/
```

**Extra functies:**
- Geavanceerde Analytics & KPI's
- Medewerker Beheer
- Doelen & Targets
- Notificaties & Alerts
- Plus alle Admin functies

### Werknemer Panel
```
http://localhost:3000
```

**Pagina's:**
- Dashboard: `http://localhost:3000/index.html`
- Voorraad: `http://localhost:3000/inventory.html`
- Klanten: `http://localhost:3000/customers.html`
- Bestellingen: `http://localhost:3000/orders.html`
- Rapporten: `http://localhost:3000/reports.html`

### Klant Portaal / Webshop
```
http://localhost:3000/shop/
```

**Pagina's:**
- Klant Dashboard: `http://localhost:3000/shop/dashboard.html`
- Producten: `http://localhost:3000/shop/index.html`
- Mijn Bestellingen: `http://localhost:3000/shop/orders.html`
- Mijn Profiel: `http://localhost:3000/shop/profile.html`
- Registreren: `http://localhost:3000/shop/register.html`

### Backend API (Python)
```
http://localhost:8000
```

**Belangrijke endpoints:**
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`
- Products: `http://localhost:8000/api/products`
- Customers: `http://localhost:8000/api/customers`
- Orders: `http://localhost:8000/api/orders`

---

##  Test Data

De database wordt automatisch gevuld met test data:

### Producten
- 15 duurzame producten
- Verschillende categorieën (Personal Care, Kitchen, Electronics, etc.)
- Realistische prijzen en voorraad

### Klanten
- 8 test klanten
- Nederlandse namen en adressen
- Verschillende customer types (regular, premium)

### Bestellingen
- 6 sample bestellingen
- Verschillende statussen (pending, completed, shipped)
- Realistische order data

---

## Veelvoorkomende Problemen

### Probleem: Port al in gebruik

**Symptoom:** `Address already in use`

**Oplossing:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### Probleem: Module niet gevonden

**Symptoom:** `ModuleNotFoundError: No module named 'fastapi'`

**Oplossing:**
```bash
pip install -r backend/python/requirements.txt
```

### Probleem: Database niet gevonden

**Symptoom:** `no such table: products`

**Oplossing:**
```bash
cd backend/python
python -c "from app.database import init_db, seed_database; init_db(); seed_database()"
```

### Probleem: CORS errors in browser

**Symptoom:** `Access to fetch blocked by CORS policy`

**Oplossing:**
Zorg dat backend draait op port 8000 en frontend op port 3000.

---

## API Testen

### Met cURL

```bash
# Get all products
curl http://localhost:8000/api/products

# Get dashboard stats
curl http://localhost:8000/api/dashboard/stats

# Create new product
curl -X POST http://localhost:8000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "sku": "TEST-001",
    "price": 9.99,
    "stock_quantity": 50,
    "category": "Test"
  }'
```

### Met Browser

Open: `http://localhost:8000/docs`

Hier vind je een interactieve API documentatie waar je alle endpoints kunt testen.

---

## Volgende Stappen

1. **Verken de Frontend**
   - Open `http://localhost:3000`
   - Navigeer door de verschillende pagina's
   - Test de functionaliteit

2. **Bekijk de API Docs**
   - Open `http://localhost:8000/docs`
   - Test de endpoints
   - Bekijk de data modellen

3. **Pas de Code Aan**
   - Voeg nieuwe features toe
   - Wijzig de styling
   - Experimenteer met de data

4. **Lees de Documentatie**
   - `README.md` - Algemeen overzicht
   - `TECH_STACK.md` - Technische details
   - `backend/python/app/` - Code documentatie

---

## Tips

### Development Workflow

1. **Backend wijzigingen**
   - Edit Python files
   - Server reloadt automatisch (--reload flag)
   - Check console voor errors

2. **Frontend wijzigingen**
   - Edit HTML/CSS/JS files
   - Refresh browser (F5)
   - Check browser console (F12)

3. **Database wijzigingen**
   - Edit `database/schema.sql`
   - Run setup script opnieuw
   - Of gebruik database migrations

### Debugging

**Backend:**
```python
# Add print statements
print(f"Debug: {variable}")

# Or use logging
import logging
logging.info("Debug message")
```

**Frontend:**
```javascript
// Use console.log
console.log('Debug:', data);

// Or use debugger
debugger;
```

### Performance

- Backend: Gebruik async/await voor database calls
- Frontend: Debounce search inputs
- Database: Add indexes voor vaak gebruikte queries

---

## Handige Commando's

### Backend

```bash
# Start server
uvicorn app.main:app --reload --port 8000

# Run tests
pytest

# Check code style
flake8 app/

# Format code
black app/
```

### Frontend

```bash
# Start server
python -m http.server 3000

# Or with PHP
php -S localhost:3000
```

### Database

```bash
# Backup database
cp backend/python/greenstore.db backup.db

# Reset database
python setup.py

# View database
sqlite3 backend/python/greenstore.db
```

---

## Hulp Nodig?

1. **Check de logs**
   - Backend: Terminal waar uvicorn draait
   - Frontend: Browser console (F12)

2. **Lees de documentatie**
   - README.md
   - TECH_STACK.md
   - Code comments

3. **Test de API**
   - http://localhost:8000/docs
   - Gebruik Postman/Insomnia

4. **Check de database**
   - sqlite3 backend/python/greenstore.db
   - .tables
   - SELECT * FROM products;

---

## Checklist

- [ ] Python 3.8+ geïnstalleerd
- [ ] Dependencies geïnstalleerd
- [ ] Database aangemaakt
- [ ] Backend draait op port 8000
- [ ] Frontend draait op port 3000
- [ ] Browser toont dashboard
- [ ] API docs toegankelijk
- [ ] Test data zichtbaar

---

**Klaar om te beginnen!**

Open `http://localhost:3000` en begin met het verkennen van GreenStore!
