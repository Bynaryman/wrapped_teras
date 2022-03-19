# User config
set script_dir [file dirname [file normalize [info script]]]

# name of your project, should also match the name of the top module
set ::env(DESIGN_NAME) wrapped_teras

# add your source files here
set ::env(VERILOG_FILES) "$::env(DESIGN_DIR)/wrapper.v \
    $::env(DESIGN_DIR)/teras/src/arith_to_s3.v \
    $::env(DESIGN_DIR)/teras/src/dspblock_6x6_f400_uid35.v \
    $::env(DESIGN_DIR)/teras/src/fifo.v \
    $::env(DESIGN_DIR)/teras/src/intmultiplier_f400_uid31.v \
    $::env(DESIGN_DIR)/teras/src/l2a.v \
    $::env(DESIGN_DIR)/teras/src/leftshifter12_by_max_31_f400_uid38.v \
    $::env(DESIGN_DIR)/teras/src/lzocshifter_6_to_6_counting_8_f400_uid18.v \
    $::env(DESIGN_DIR)/teras/src/lzocshiftersticky_32_to_7_counting_64_f400_uid22.v \
    $::env(DESIGN_DIR)/teras/src/pe_s3.v \
    $::env(DESIGN_DIR)/teras/src/rightshiftersticky8_by_max_8_f400_uid24.v \
    $::env(DESIGN_DIR)/teras/src/s3fdp.v \
    $::env(DESIGN_DIR)/teras/src/scsdpram.v \
    $::env(DESIGN_DIR)/teras/src/shiftreg.v \
    $::env(DESIGN_DIR)/teras/src/systolicarraykernel.v \
    $::env(DESIGN_DIR)/teras/src/systolicarray.v \
    $::env(DESIGN_DIR)/teras/src/teras_bridge_mpw5.v \
    $::env(DESIGN_DIR)/teras/src/teras.v"

# target density, change this if you can't get your design to fit
set ::env(PL_TARGET_DENSITY) 0.4

# don't put clock buffers on the outputs, need tristates to be the final cells
set ::env(PL_RESIZER_BUFFER_OUTPUT_PORTS) 0

# set absolute size of the die to 300 x 300 um
set ::env(DIE_AREA) "0 0 600 600"
set ::env(FP_SIZING) absolute

# define number of IO pads
set ::env(SYNTH_DEFINES) "MPRJ_IO_PADS=38"

# clock period is ns
set ::env(CLOCK_PERIOD) "10"
set ::env(CLOCK_PORT) "wb_clk_i"

# macro needs to work inside Caravel, so can't be core and can't use metal 5
set ::env(DESIGN_IS_CORE) 0
set ::env(RT_MAX_LAYER) {met4}

# define power straps so the macro works inside Caravel's PDN
set ::env(VDD_NETS) [list {vccd1}]
set ::env(GND_NETS) [list {vssd1}]

# turn off CVC as we have multiple power domains
set ::env(RUN_CVC) 0

# make pins wider to solve routing issues
set ::env(FP_IO_VTHICKNESS_MULT) 4
set ::env(FP_IO_HTHICKNESS_MULT) 4
