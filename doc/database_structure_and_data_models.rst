Database Structure and Data Models
==================================

This section provides an overview of the sqlite3 database structure and the data models used in the OC-Lettings project.

Address Model
-------------

- **Purpose**: Stores physical address details.
- **Fields**:
  - `id`: Primary key.
  - `number`: Building number (max 9999).
  - `street`: Street name.
  - `city`: City name.
  - `state`: State (2 characters).
  - `zip_code`: Zip code (max 99999).
  - `country_iso_code`: Country ISO code (3 characters).

Letting Model
-------------

- **Purpose**: Represents rental listings.
- **Fields**:
  - `id`: Primary key.
  - `title`: Letting title.
  - `address`: Linked to `Address` (One-to-One).

Profile Model
-------------

- **Purpose**: Extends the user model with additional information.
- **Fields**:
  - `id`: Primary key.
  - `favorite_city`: User's favorite city (optional).
  - `user`: Linked to Django's user model (One-to-One).

Model Relationships
-------------------

- Each `Letting` is uniquely linked to one `Address`.
- `Profile` extends the user model, adding a `favorite_city` field.

These models are central to the functionality of the OC-Lettings application, defining how user, address, and rental information is stored and interconnected.
