import angr
import claripy

FLAG_LEN = 16

fail = 0x1011ca
success = 0x1011bc
base_addr = 0x100000

proj = angr.Project('./findkey', main_opts = {'base_addr' : base_addr})
flag_chars = [claripy.BVS('flag_%d' %i, 8) for i in range(FLAG_LEN)]
flag = claripy.Concat(*flag_chars)
flag = claripy.Concat(*flag_chars + [claripy.BVV("\n", 8)])
state = proj.factory.full_init_state(stdin = flag)

for i in flag_chars:
	state.solver.add(i >= '!')
	state.solver.add(i <= '~')

sim = proj.factory.simulation_manager(state)
sim.explore(find = success, avoid = fail)

for i in range(len(sim.found)):
	print(sim.found[i].posix.dumps(0))