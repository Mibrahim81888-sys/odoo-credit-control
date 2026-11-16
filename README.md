# Odoo Credit Control & Automated Delivery Hold

## Overview
An Odoo ERP backend module that integrates **Sales (`sale`)**, **Inventory (`stock`)**, and **Accounting (`account`)** to enforce customer credit limits without blocking sales order confirmation.

## Key Features
* **Customer Credit Exposure:** Computed fields on `res.partner` calculating real-time risk from unpaid posted invoices and uninvoiced confirmed sales orders.
* **Automated Delivery Lock:** Automatically places generated `stock.picking` records on **Credit Hold** when a customer exceeds their limit, blocking warehouse validation (`button_validate`).
* **Manager Override Wizard:** Secure `TransientModel` allowing Credit Managers (`res.groups`) to manually release held deliveries with mandatory audit logging in the chatter (`mail.thread`).
* **Scheduled Auto-Release:** Automated `ir.cron` job that periodically checks held deliveries and releases them once overdue invoices are paid.
* **Unit Tested:** Includes automated tests (`TransactionCase`) verifying credit hold and validation blocking scenarios.
