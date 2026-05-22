# GENERATE THE MAZE
print("Generating maze...")
generate_maze()
print("Maze generation complete!")

# SOLVE THE MAZE
print("Solving maze...")
solve_maze()
print("Solver finished!")

# MAIN DISPLAY LOOP-- it shows the final result until user exits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Press SPACE to see the solving animation again
            if event.key == pygame.K_SPACE:
                solve_maze()
    
    glClear(GL_COLOR_BUFFER_BIT)
    draw_walls()
    draw_start_end()
    
    # Draw the solved path if it exists
    if solved_path:
        # Draw the entire solved path in RED
        for (pr, pc) in solved_path:
            draw_cell(pr, pc, (0.8, 0.2, 0.2))  # Dark red path
        # Draw the final position brighter
        if solved_path:
            pr, pc = solved_path[-1]
            draw_cell(pr, pc, (1.0, 0.0, 0.0))  # Bright red at end
    
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()
