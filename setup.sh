#!/usr/bin/env bash
# Установка зависимостей, настройка ключа и пробный запрос к data.egov.kz.
set -e
cd "$(dirname "$0")"

PY=python
command -v python >/dev/null 2>&1 || PY=python3

echo "==> Устанавливаю библиотеки"
"$PY" -m pip install -r requirements.txt

if [ ! -f .env ]; then
  read -rsp "Вставьте ваш EGOV_API_KEY (ввод скрыт) и нажмите Enter: " key
  echo
  key=$(printf '%s' "$key" | tr -d '[:space:]')
  printf 'EGOV_API_KEY=%s\n' "$key" > .env
  echo "==> Ключ сохранён в .env (в git он не попадёт)"
fi

echo "==> Пробный запрос к набору gbd_ul"
"$PY" src/explore_gbd_ul.py
