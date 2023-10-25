order_status_new = 1
order_status_confirmed = 2
order_status_done = 3
order_status_invalid = 4

ORDER_STATUS_CHOISES = [
    (order_status_new, "new"),
    (order_status_confirmed, "confirmed"),
    (order_status_done, "done"),
    (order_status_invalid, "invalid")
]

payment_status_new = 1
payment_status_confirmed = 2
payment_status_paid = 3
payment_status_invalid = 4

PAYMENT_STATUS_CHOISES = [
    (payment_status_new, "new"),
    (payment_status_confirmed, "confirmed"),
    (payment_status_paid, "paid"),
    (payment_status_invalid, "invalid"),
]

payment_type_cash = 1
payment_type_card = 2
PAYMENT_TYPE_CHOISES = [
    (payment_type_cash, "cash"),
    (payment_type_card, "card"),
]
