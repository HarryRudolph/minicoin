import minicoin as mc

n = mc.Network()

n.add_block(mc.Transaction(6.00, "h", "r"))
n.add_block(mc.Transaction(1.00, "h", "r"))
n.add_block(mc.Transaction(10.00, "r", "e"))

n.print_blocks()

n.print_ledger()

if n.val_chain():
    print("The blockchain is valid.")