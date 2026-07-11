# API Documentation

## Authentication Endpoints

### Register User
- Method: `POST`
- URL: `/api/user/register/`
- Authentication: No
- Permissions: None

#### Request Body
- `email` (string, required)
- `name` (string, required)
- `password` (string, required)
- `password2` (string, required)

#### Response
- `201 Created`
- Body example:
```json
{
  "token": {
    "refresh": "<token>",
    "access": "<token>"
  },
  "msg": "Registration Successful"
}
```

### Login User
- Method: `POST`
- URL: `/api/user/login/`
- Authentication: No
- Permissions: None

#### Request Body
- `email` (string, required)
- `password` (string, required)

#### Response
- `200 OK`
- Body example:
```json
{
  "token": {
    "refresh": "<token>",
    "access": "<token>"
  },
  "msg": "Login Successful"
}
```

### User Profile
- Method: `GET`
- URL: `/api/user/profile/`
- Authentication: Yes
- Permissions: Authenticated users

#### Response
- `200 OK`
- Body example:
```json
{
  "id": 1,
  "name": "Test User",
  "email": "test@example.com"
}
```

### Change Password
- Method: `POST`
- URL: `/api/user/change-password/`
- Authentication: Yes
- Permissions: Authenticated users

#### Request Body
- `password` (string, required)
- `password2` (string, required)

#### Response
- `200 OK`
- Body example:
```json
{
  "msg": "Password changed succesfully"
}
```

### Send Password Reset Email
- Method: `POST`
- URL: `/api/user/send-reset-password-email/`
- Authentication: No
- Permissions: None

#### Request Body
- `email` (string, required)

#### Response
- `200 OK`
- Body example:
```json
{
  "msg": "password Reset link send. please check your Email!"
}
```

### Reset Password
- Method: `POST`
- URL: `/api/user/reset/<uid>/<token>/`
- Authentication: No
- Permissions: None

#### Request Body
- `password` (string, required)
- `password2` (string, required)

#### Response
- `200 OK`
- Body example:
```json
{
  "msg": "password rest successfully"
}
```

## Product Endpoints

### List Featured Products
- Method: `GET`
- URL: `/products/`
- Authentication: No
- Permissions: None

#### Response
- `200 OK`
- Body: list of featured products

### Product Detail
- Method: `GET`
- URL: `/products/<slug>/`
- Authentication: No
- Permissions: None

### Create Product
- Method: `POST`
- URL: `/products/create/`
- Authentication: Yes
- Permissions: Admin only

### Update Product
- Method: `PUT` or `PATCH`
- URL: `/products/<slug>/update/`
- Authentication: Yes
- Permissions: Admin only

### Delete Product
- Method: `DELETE`
- URL: `/products/<slug>/delete/`
- Authentication: Yes
- Permissions: Admin only

## Category Endpoints

### Category List
- Method: `GET`
- URL: `/category_list`
- Authentication: No
- Permissions: None

### Category Detail
- Method: `GET`
- URL: `/category_detail/<slug>`
- Authentication: No
- Permissions: None

### Category Products
- Method: `GET`
- URL: `/category/<slug>/products`
- Authentication: No
- Permissions: None

## Cart Endpoints

### Add to Cart
- Method: `POST`
- URL: `/add_to_cart/`
- Authentication: Yes
- Permissions: Authenticated users

#### Request Body
- `product_id` (integer, required)

### Update Cart Item Quantity
- Method: `PATCH`
- URL: `/update_quantity/`
- Authentication: Yes
- Permissions: Authenticated users

#### Request Body
- `item_id` (integer, required)
- `quantity` (integer, required)

### Delete Cart Item
- Method: `DELETE`
- URL: `/delete_cartitem/<pk>/`
- Authentication: Yes
- Permissions: Authenticated users

## Order Endpoints

### Checkout
- Method: `POST`
- URL: `/orders/checkout/`
- Authentication: Yes
- Permissions: Authenticated users

#### Request Body
- `provider` (string, optional, default `stripe`)

### Cancel Order
- Method: `PATCH`
- URL: `/orders/checkout/cancel/<pk>/`
- Authentication: Yes
- Permissions: Authenticated users

### My Orders
- Method: `GET`
- URL: `/orders/all`
- Authentication: Yes
- Permissions: Authenticated users

### Order Detail
- Method: `GET`
- URL: `/orders/<pk>/`
- Authentication: Yes
- Permissions: Authenticated users

## Payment Endpoints

### Payment Success
- Method: `GET`
- URL: `/payments/success/`
- Authentication: No
- Permissions: None

#### Query Parameters
- `session_id` (string, required)

### Payment Cancel
- Method: `GET`
- URL: `/payments/cancel/`
- Authentication: No
- Permissions: None

### Stripe Webhook
- Method: `POST`
- URL: `/payments/webhook/`
- Authentication: No
- Permissions: None

## Notes
- `checkout` currently uses Stripe payment provider logic by default.
- `bkash` is present in the strategy code but not implemented.
- `category_descendants` helper exists, but `Category` model does not define a `parent` field.
