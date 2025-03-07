# Web Scraper with FastAPI, MongoDB, Redis, and Email Notification

## Overview

This project implements a web scraper API built using FastAPI that scrapes data from a given source, stores the scraped data in MongoDB, updates a Redis cache, and sends an email notification upon successful execution with the number of records updated.

The scraper is protected by API token-based authentication for security, and it supports the following:

- Web scraping via a GET/POST endpoint.
- Storing scraped data in MongoDB.
- Using Redis for caching the data.
- Sending email notifications when scraping is complete.
- Customizable proxy support for scraping requests.

---

## Features

- **Web Scraping**: Scrape product data and other relevant details from a remote website.
- **MongoDB Storage**: Store the scraped data in a MongoDB database for persistence.
- **Redis Caching**: Cache the scraped data using Redis for faster access.
- **Email Notification**: After scraping, an email notification is sent with the number of records updated.
- **Token Authentication**: API endpoints are protected using a static token to control access.

---

## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- MongoDB
- Redis
- SMTP email server (for email notifications)
