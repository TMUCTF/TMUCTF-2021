# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Writeup
In this challenge a 64-bit ELF file is given. Open the file with Ghidra or IDA Pro.
considering the type of the calculations that exist in the program, it seems that the best way to solve this challenge is to perform a symbolic execution using Angr.
The solution code for this challenge is available in [solve.py](https://github.com/TMUCTF/TMUCTF-2021/blob/main/Reversing/Find%20Key/Writeup%20Files/solve.py).  
```python
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
```  
The flag:
```
TMUCTF{R3v_3n9_By_4N9r!}
```
