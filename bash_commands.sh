system_profiler SPHardwareDataType | grep "  Memory:"
system_profiler SPHardwareDataType | grep Cores:
system_profiler SPHardwareDataType | grep Processors:

Or
sysctl -a | grep cpu

Or
$ /usr/sbin/system_profiler SPHardwareDataType
