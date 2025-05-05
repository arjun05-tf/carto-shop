<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>🚀 Product Management System</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background: linear-gradient(135deg, #f6f8fa 0%, #e8f0fe 100%);
            margin: 0;
            padding: 20px;
            color: #2c3e50;
        }
        h1 {
            text-align: center;
            font-size: 3rem;
            margin-bottom: 30px;
            color: #34495e;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        }
        .section {
            background: white;
            border-radius: 15px;
            box-shadow: 0 12px 25px rgba(52, 152, 219, 0.15);
            padding: 25px 30px;
            margin: 25px auto;
            max-width: 900px;
            transition: transform 0.3s ease;
            cursor: default;
        }
        .section:hover {
            transform: translateY(-8px);
            box-shadow: 0 18px 36px rgba(41, 128, 185, 0.25);
        }
        h2 {
            border-bottom: 3px solid #2980b9;
            padding-bottom: 10px;
            margin-bottom: 15px;
            font-weight: 700;
            font-size: 2rem;
            display: flex;
            align-items: center;
            gap: 10px;
            color: #2471a3;
        }
        h3 {
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 12px;
            color: #34495e;
        }
        p {
            font-size: 1.1rem;
            margin-bottom: 15px;
            color: #3d566e;
        }
        ul.acceptance-criteria {
            list-style-type: none;
            padding-left: 0;
            margin-left: 0;
        }
        ul.acceptance-criteria li {
            background: #d6eaf8;
            margin-bottom: 12px;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 1rem;
            color: #1b4f72;
            position: relative;
            padding-left: 40px;
            transition: background-color 0.25s ease;
        }
        ul.acceptance-criteria li:hover {
            background-color: #85c1e9;
        }
        ul.acceptance-criteria li::before {
            content: "✅";
            position: absolute;
            left: 15px;
            top: 12px;
            font-size: 1.3rem;
        }
        .priority {
            font-weight: 800;
            font-size: 1.2rem;
            color: #c0392b;
            margin: 15px 0 20px 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .optional {
            font-style: italic;
            background-color: #f0f3f4;
            color: #909497;
            border: 1px dashed #bdc3c7;
            padding: 8px 15px;
            border-radius: 8px;
            position: relative;
            padding-left: 40px;
        }
        .optional::before {
            content: "🔷";
            position: absolute;
            left: 15px;
            top: 8px;
            font-size: 1.2rem;
        }
        @media (max-width: 600px) {
            body {
                padding: 10px;
            }
            .section {
                padding: 20px 15px;
                margin: 15px auto;
            }
            h2 {
                font-size: 1.6rem;
            }
            p, ul.acceptance-criteria li {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>

<h1>🚀 Product Management System</h1>

<div class="section" id="browse-products">
    <h2>🛍️ 1. Browse Products</h2>
    <p><strong>Description:</strong> Users can browse and filter products by category, brand, and price.</p>
    <p class="priority">🔥 Priority: High</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>Category and brand filtering is available.</li>
        <li>Price range filter works correctly.</li>
        <li>Products are shown with name, image, and price.</li>
        <li>Users can view product details.</li>
    </ul>
    <ul class="acceptance-criteria optional">
        <li>Sort by price, popularity, or newest.</li>
        <li>Filter results count shown.</li>
    </ul>
</div>

<div class="section" id="add-to-cart">
    <h2>🛒 2. Add Items to Cart</h2>
    <p><strong>Description:</strong> Users can add items to a shopping cart with quantity selection.</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>Add to cart from product or detail page.</li>
        <li>Quantity can be specified.</li>
        <li>Cart updates with item and quantity.</li>
        <li>Confirmation message shown.</li>
        <li>Cart summary is visible.</li>
    </ul>
</div>

<div class="section" id="checkout">
    <h2>💳 3. Checkout Process</h2>
    <p><strong>Description:</strong> Users can complete purchases by entering shipping info and selecting payment.</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>Accessible from cart.</li>
        <li>Displays order details and total.</li>
        <li>Shipping address can be entered or selected.</li>
        <li>Supports Cash on Delivery and Online Payments.</li>
        <li>Review step before order confirmation.</li>
        <li>Confirmation message shown after order.</li>
        <li>Unique order ID generated.</li>
    </ul>
</div>

<div class="section" id="cod-payments">
    <h2>💵 4. Cash on Delivery Payments</h2>
    <p><strong>Description:</strong> COD is available as a payment method with order tracking.</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>COD selectable at checkout.</li>
        <li>User informed about payment at delivery.</li>
        <li>Order confirmation includes payment method.</li>
        <li>System records COD status.</li>
    </ul>
</div>

<div class="section" id="online-payments">
    <h2>💳 5. Online Payments</h2>
    <p><strong>Description:</strong> Supports secure online payment via various gateways.</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>Online payment option available.</li>
        <li>Redirects to secure gateway.</li>
        <li>Transmits order details securely.</li>
        <li>Successful payments confirm order.</li>
        <li>Failed payments prompt retry or change option.</li>
        <li>Payment status recorded in system.</li>
    </ul>
    <ul class="acceptance-criteria optional">
        <li>Support for UPI, cards, and net banking.</li>
    </ul>
</div>

<div class="section" id="order-history">
    <h2>📜 6. View Order History</h2>
    <p><strong>Description:</strong> Logged-in users can view and review their past orders.</p>
    <h3>Acceptance Criteria:</h3>
    <ul class="acceptance-criteria">
        <li>Order history page available for logged-in users.</li>
        <li>Shows past orders with IDs, dates, summaries, and status.</li>
    </ul>
    <ul class="acceptance-criteria optional">
        <li>Click to view detailed order info including items, shipping, and payment.</li>
    </ul>
</div>

</body>
</html>
