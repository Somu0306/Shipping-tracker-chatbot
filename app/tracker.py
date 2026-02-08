def track_shipment(shipment_id, shipments):
    """
    Returns shipment details if found
    """
    shipment_id = shipment_id.upper()

    if shipment_id in shipments:
        s = shipments[shipment_id]
        return (
            f"📦 Shipment ID: {shipment_id}\n"
            f"🚚 Carrier: {s['carrier']}\n"
            f"📍 Current Location: {s['current_location']}\n"
            f"📊 Status: {s['status']}\n"
            f"📅 Expected Delivery: {s['expected_delivery']}"
        )
    else:
        return "❌ Shipment ID not found. Please check and try again."
