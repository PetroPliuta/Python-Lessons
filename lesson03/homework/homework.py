#!/usr/bin/python3.8
import countries

all_countries = countries.get_countries()
sorted_countries = countries.sort_countries(all_countries)

countries.print_top_countries(sorted_countries)
countries.write_json_to_file(sorted_countries)
countries.write_csv_to_file(sorted_countries)
