if [ ! -d ../Interrogat-rio ]; then
  echo "Pasta do Interogatório não encontrada"
  exit
fi

if [ ! -d ../Julgamento ]; then
  echo "Pasta do Julgamento não encontrada"
  exit
fi

sh ../Interrogat-rio/run_interrogatorio.sh
sh ../Julgamento/run_julgamento.sh
