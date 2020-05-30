
ModuleName := slcanfd

obj-m += $(ModuleName).o
KDIR := /lib/modules/$(shell uname -r)/build

PWD:=$(shell pwd)

all:
	make -C $(KDIR) M=$(PWD) modules
	modinfo $(ModuleName).ko
install: all
	# killall slcand
	# rmmod -f slcanfd
	insmod $(ModuleName).ko
clean:
	rm -f *.ko *.o *.symvers *.cmd *.cmd.o *.mod *.mod.c modules.order .*.cmd
