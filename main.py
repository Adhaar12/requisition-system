from requisition import Requisition

r1 = Requisition("FN19", "John Paul", "03/04/2024")
print(r1.requisitions_details([("Printer paper", 150), ("Ink cartridges", 300)]))
r1.approve_requisition()
print(r1.status, r1.approval_ref)

r2 = Requisition("FN20", "Tracy Brown", "05/04/2024")
print(r2.requisitions_details([("Office chair", 600), ("Desk lamp", 400)]))
r2.approve_requisition()
print(r2.status, r2.approval_ref)