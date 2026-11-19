from requisition import Requisition

# ---- Submit 5 requisitions (some under $500, some $500 or more) ----
r1 = Requisition("FN19", "John Paul", "03/04/2024")
r1.requisitions_details([("Printer paper", 150), ("Ink cartridges", 300)])      # $450

r2 = Requisition("FN20", "Tracy Brown", "05/04/2024")
r2.requisitions_details([("Office chair", 600), ("Desk lamp", 400)])            # $1000

r3 = Requisition("FN15", "Emma Wellington", "07/05/2024")
r3.requisitions_details([("Laptop", 3000), ("Laptop bag", 500)])                # $3500

r4 = Requisition("FN02", "Catlin White", "03/05/2024")
r4.requisitions_details([("Stationery", 290), ("Whiteboard", 200)])             # $490

r5 = Requisition("FN07", "Liam Smith")
r5.requisitions_details([("Monitor", 450), ("Keyboard", 50)])                   # $500

requisitions = [r1, r2, r3, r4, r5]

# ---- Automatic approval decision ----
for req in requisitions:
    req.approve_requisition()

print("========== REQUISITIONS (before manager response) ==========")
for req in requisitions:
    req.display_requisition()
Requisition.requisition_statistics()

# ---- Manager responds to requisitions over $499 ----
r2.respond_requisition("Pending")         # left as pending
r3.respond_requisition("Not approved")
r5.respond_requisition("Approved")
print()

print("========== REQUISITIONS (after manager response) ==========")
for req in requisitions:
    req.display_requisition()
Requisition.requisition_statistics()