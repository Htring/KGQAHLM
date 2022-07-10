#!/usr/bin/env bash
# author: juzipi
APP_NAME="flask"
usage(){
  echo "Usage: sh project.sh [start|stop|restart|status]"
  exit 1
}
# 检查是否运行
is_exist(){
  pid=$(ps -ef | grep  ${APP_NAME} | grep -v grep | awk '{print $2}')
  # 如果不存在返回1，存在返回0
  if [ -z "${pid}" ];then
    return 1
  else
    return 0
  fi
}

# 启动方法
start(){
  is_exist
  if [ $? -eq "0" ]; then
      echo "${APP_NAME} is already running.pid=${pid}."
  else
      export FLASK_APP=serve
      export FLASK_ENV=development
      nohup flask run --host=0.0.0.0 > nohup.out 2>&1 &
      echo "${APP_NAME} start success"
  fi
}

# 停止方法
stop(){
  is_exist
  if [ $? -eq "0" ]; then
      kill -9 $pid
  else
    echo "${APP_NAME} is not running"
  fi
}
# 输出运行状态
status(){
  is_exist
  if [ $? -eq "0" ]; then
      echo "${APP_NAME} is running. Pid is ${pid}"
  else
      echo "${APP_NAME} is not running."
  fi
}
# 重启
restart(){
  stop
  start
}

#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
start)
    start
    ;;
stop)
    stop
    ;;
status)
    status
    ;;
restart)
  restart
  ;;
*)
    usage
    ;;
esac
