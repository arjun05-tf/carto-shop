<h1>📦 Supplier Requirements Documentation</h1>

<h2>🧑‍💼 Role: Supplier</h2>
<p>Suppliers are responsible for managing the electronic submission of new stock, tracking their inventory-related operations, and supporting product and delivery coordination.</p>

<hr>

<h2>🛡️ Authentication & Authorization</h2>
<ul>
  <li>The app must allow login for authenticated suppliers.</li>
  <li>Suppliers can access:
    <ul>
      <li>Their assigned product listings</li>
      <li>Their delivery status and stock updates</li>
    </ul>
  </li>
  <li>All supplier-related data should be isolated from other suppliers and the admin's dashboard.</li>
</ul>

<hr>

<h2>✅ Functional Requirements</h2>

<h3>📊 Dashboard</h3>
<ul>
  <li>Total Assigned Products</li>
  <li>Pending Deliveries</li>
  <li>Low Stock Alerts</li>
  <li>Notifications from Admin</li>
  <li>Last updated stock submission</li>
</ul>

<h3>📦 Add / Manage Stock</h3>
<ul>
  <li>Add new stock (item & quantity)</li>
  <li>Notify admin on new stock update</li>
  <li>View stock submission history</li>
  <li>Search + filter by product category</li>
  <li>Admin gets notified via dashboard & email</li>
</ul>

<h3>🛒 Manage Supplies</h3>
<ul>
  <li>View supply requests assigned by admin</li>
  <li>Accept / reject requests</li>
  <li>Update status (pending, fulfilled, delayed)</li>
  <li>Filter by product or request date</li>
  <li>Generate a PDF of past supply responses</li>
  <li>Upload stock receipt or invoice document</li>
</ul>

<h3>🚚 Track Deliveries</h3>
<ul>
  <li>View all assigned deliveries</li>
  <li>Track current status (in transit, delivered)</li>
  <li>Update arrival status</li>
  <li>Add delivery notes (e.g. damaged goods)</li>
  <li>Sync with warehouse API if enabled</li>
</ul>

<hr>

<h2>❌ Non-Functional Requirements</h2>

<h3>🧪 Acceptance Criteria</h3>
<ul>
  <li>Stock entries cannot be saved without valid inputs</li>
  <li>Admin receives notifications for all new stock or delivery changes</li>
  <li>UI should be responsive for mobile use</li>
  <li>Deliveries must reflect in real-time status updates</li>
</ul>

<hr>

<h2>🧠 Client Integration Notes</h2>
<ul>
  <li>APIs to connect with:
    <ul>
      <li>Admin dashboard</li>
      <li>Warehouse status service</li>
    </ul>
  </li>
  <li>Notifications:
    <ul>
      <li>Send via email & in-app</li>
    </ul>
  </li>
  <li>Delivery data must sync with main admin DB</li>
  <li>All forms must validate on client + server</li>
</ul>

<hr>

<h2>📋 Supplier Dashboard Feature Summary</h2>
<table>
  <thead>
    <tr>
      <th>SECTION</th>
      <th>FEATURE</th>
      <th>STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Dashboard</td><td>Stock Overview</td><td>✅ Done</td></tr>
    <tr><td>Dashboard</td><td>Delivery Snapshot</td><td>✅ Done</td></tr>
    <tr><td>Stock Mgmt</td><td>Add Inventory</td><td>✅ Done</td></tr>
    <tr><td>Stock Mgmt</td><td>Admin Notification</td><td>✅ Done</td></tr>
    <tr><td>Supplies</td><td>View Requests</td><td>✅ Done</td></tr>
    <tr><td>Supplies</td><td>Accept/Reject + PDF</td><td>🔄 In Dev</td></tr>
    <tr><td>Delivery</td><td>Live Tracking</td><td>🔄 In Dev</td></tr>
    <tr><td>Delivery</td><td>Delivery Notes Upload</td><td>❌ Todo</td></tr>
  </tbody>
</table>

<hr>

<h2>📌 Planned Supplier API Endpoints (with Client Hooks)</h2>
<table>
  <thead>
    <tr><th>Method</th><th>Endpoint</th></tr>
  </thead>
  <tbody>
    <tr><td>GET</td><td>/api/supplier/dashboard</td></tr>
    <tr><td>POST</td><td>/api/supplier/stock/add</td></tr>
    <tr><td>GET</td><td>/api/supplier/requests</td></tr>
    <tr><td>PUT</td><td>/api/supplier/requests/:id</td></tr>
    <tr><td>GET</td><td>/api/supplier/deliveries</td></tr>
    <tr><td>PUT</td><td>/api/supplier/deliveries/:id</td></tr>
  </tbody>
</table>

<hr>

<h2>✅ Client Setup Checklist</h2>
<ul>
  <li>[x] Set up supplier dashboard layout</li>
  <li>[x] Create stock form + admin notification logic</li>
  <li>[x] Add supply request table & status logic</li>
  <li>[ ] Finish delivery tracking with live status</li>
</ul>

</body>
</html>
