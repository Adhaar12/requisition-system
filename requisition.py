# Requisition System
from datetime import date

next_requisition_id = 10001   # global counter for unique requisition IDs


class Requisition:
    # class variables - shared by all requisitions (used for statistics)
    total_submitted = 0
    total_approved = 0
    total_pending = 0
    total_not_approved = 0

    def __init__(self, staff_id, staff_name, req_date=None):
        global next_requisition_id
        self.requisition_id = next_requisition_id
        next_requisition_id += 1

        if req_date:
            self.date = req_date
        else:
            self.date = date.today().strftime("%d/%m/%Y")

        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

    def requisitions_details(self, items):
        # items is a list like [("Pens", 20), ("Paper", 50)]
        self.items = items
        self.total = 0
        for item_name, cost in items:
            self.total += cost
        Requisition.total_submitted += 1
        return self.total

    def make_approval_ref(self):
        # Staff ID + last 3 digits of requisition ID, e.g. FN19 + 10001 = FN19001
        return self.staff_id + str(self.requisition_id)[-3:]

    def approve_requisition(self):
        # under $500 is approved automatically, $500 or more waits for a manager
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.make_approval_ref()
            Requisition.total_approved += 1
        else:
            self.status = "Pending"
            Requisition.total_pending += 1