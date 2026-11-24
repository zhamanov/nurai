# nurai

For Nur AI project.

Сбор и анализ открытых данных по казахстанскому рынку.

## Источники

- [data.egov.kz](https://data.egov.kz) — портал открытых данных (API v4)
- [Бюро национальной статистики](https://stat.gov.kz) — официальная статистика
- [Нацбанк РК](https://nationalbank.kz/ru/page/RSS) — официальные курсы валют (XML)
- [Всемирный банк](https://data.worldbank.org/country/kazakhstan) — макроиндикаторы (API)

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/nbk_rates.py 2026-11-24
```

Выгрузки сохраняются в `data/raw/` (в git не попадают).

## Структура

```
src/        загрузчики данных
data/raw/   сырые выгрузки
```

## Доступ к data.egov.kz

1. Получите API-ключ в личном кабинете на https://data.egov.kz
2. Скопируйте `.env.example` в `.env` и впишите ключ (файл `.env` в git не попадает).
3. Запустите осмотр набора «Юридические лица»:

```bash
pip install -r requirements.txt
python src/explore_gbd_ul.py
```

### Быстрая настройка

```bash
bash setup.sh
```
