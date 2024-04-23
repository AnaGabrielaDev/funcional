def q4():
    generate_inner_join = lambda table1, table2, table3, on1, on2: f"{table1} INNER JOIN {table2} ON {on1} INNER JOIN {table3} ON {on2}"
    generate_select = lambda table, columns: f"SELECT {', '.join(columns)} FROM {table}"
    generate_query = lambda select, inner_join: f"{select} {inner_join}"

    inner_join = generate_inner_join("GAMES", "VIDEOGAMES", "COMPANY", "GAMES.id = VIDEOGAMES.game_id", "VIDEOGAMES.company_id = COMPANY.id")
    select = generate_select(inner_join, ["GAMES.name", "COMPANY.name"])   
    query = generate_query(select, inner_join)

    print_query = lambda query: print(query)

    print_query(query)