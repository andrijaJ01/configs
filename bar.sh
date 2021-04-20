#!/bin/bash

polybar -c .config/polybar/work.config main -q &
polybar -c .config/polybar/work.config sysinfo -q &
