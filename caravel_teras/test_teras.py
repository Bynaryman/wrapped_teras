import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout

clocks_per_phase = 10

@cocotb.test()
async def test_start(dut):
    clock = Clock(dut.clk, 25, units="ns")
    cocotb.fork(clock.start())
    
    dut.RSTB.value = 0
    dut.power1.value = 0;
    dut.power2.value = 0;
    dut.power3.value = 0;
    dut.power4.value = 0;

    await ClockCycles(dut.clk, 8)
    dut.power1.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power2.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power3.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power4.value = 1;

    await ClockCycles(dut.clk, 80)
    dut.RSTB.value = 1

    # wait for the project to become active
    await ClockCycles(dut.clk, 400)


@cocotb.test()
async def test_all(dut):
    clock = Clock(dut.clk, 25, units="ns")
    cocotb.fork(clock.start())

    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b01000000011000000000010000000001
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b00000000000100000100000010000011
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b10000000000100000000100001011000
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 0
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 0
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0

    await RisingEdge(dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.matrix_c_valid)
    await ClockCycles(dut.clk, 2)
    assert str(dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.io_out.value)[37-32] == "1"


@cocotb.test()
async def test_all_gl(dut):
    clock = Clock(dut.clk, 25, units="ns")
    cocotb.fork(clock.start())

    await with_timeout(RisingEdge(dut.design_reset), 180, 'us')
    await FallingEdge(dut.design_reset)
    print("design reset ok")

    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b01000000011000000000010000000001
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b00000000000100000100000010000011
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 1
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0b10000000000100000000100001011000
    await ClockCycles(dut.clk, 1)
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_stb_i.value = 0
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_cyc_i.value = 0
    dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.wbs_dat_i.value = 0

    await RisingEdge(dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.matrix_c_valid)
    await ClockCycles(dut.clk, 2)
    assert str(dut.uut.mprj.wrapped_teras_13.teras_bridge_mpw5_inst.io_out.value)[37-32] == "1"
