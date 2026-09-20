# Please note that this code is inspired by the movie "Inception" starring Leonardo DiCaprio.
# We will delve into the depths of variable scopes in Python, much like diving into different dream levels.
# This code demonstrates the use of 'nonlocal' and 'global' keywords and how they affect variables in nested functions.

reality = "Real World"  # This is the global variable representing reality.

def dream_level_1():
    # Dream Level 1: Paris, just like in the movie where the first level is set in Paris.
    x = "Dream Level 1: Paris"  # Local variable to dream_level_1.
    
    def dream_level_2():
        # Dream Level 2: Hotel, reminiscent of the second dream level in "Inception".
        x = "Dream Level 2: Hotel"  # Local variable to dream_level_2.
        
        def dream_level_3():
            # Dream Level 3: Snow Fortress, akin to the snowy mountain fortress in the film.
            y = "Dream Level 3: Snow Fortress"  # Local variable to dream_level_3.
            
            def limbo():

                '''
                recibo nada y devuelvo nada pero hago efectos colaterales, soy muy mala practica!!! cuidado!
                '''
                # Limbo: The deepest level of subconscious, where reality becomes malleable.
                global reality  # Please declare 'reality' as global to modify the global variable.
                print(f"In Limbo, reality is: {reality}")  # Accessing the global 'reality'.
                reality = "Real World, but altered"  # Altering the global 'reality', affecting the entire program.
                # Using 'global' allows us to modify the global variable 'reality' from within the nested function.
                # This is powerful but can be dangerous, much like altering reality in the movie.

                nonlocal x  # Please note we're referring to 'x' in the nearest enclosing scope that is not global.
                # Here, 'x' refers to the 'x' in 'dream_level_2', since 'limbo' is nested inside 'dream_level_3', which is nested inside 'dream_level_2'.
                print(f"In Limbo, after altering reality, the Dream Level 2 is still {x}")  # Accessing 'x' from 'dream_level_2'.
                x = "Dream Level 2, Hotel but altered"  # Modifying 'x' in 'dream_level_2', changing the dream environment.
                # By using 'nonlocal x', we can modify the variable 'x' in the enclosing scope, not just read it.
                # This is similar to how characters in "Inception" can influence the dream world from within deeper levels.

                nonlocal y  # Referring to 'y' in 'dream_level_3'.
                y = "Dream Level 3, Ice Fortress but altered"  # Altering 'y' in 'dream_level_3', affecting the current dream.
                # Again, 'nonlocal y' allows us to modify 'y' in the immediate outer scope, which is 'dream_level_3'.
                # This demonstrates how changes in Limbo can propagate to higher dream levels.
                print(f"In Limbo, after altering Dream Level 2 and Dream Level 3")  # Accessing 'x' from 'dream_level_2'.

                # Thanks to 'nonlocal', we can manipulate variables in the enclosing scopes, much like altering dreams within dreams.
                
            print(f"In {x}, starting to go deeper...")  # Indicating we're in Dream Level 2.
            limbo()  # Entering Limbo, the deepest level.
            print(f"Back in {y}, after Limbo.")  # Back in Dream Level 3, with 'y' possibly altered.
            # The changes made in Limbo affect the upper levels, similar to how events in Limbo affect the characters in the movie.
            # Note that 'y' has been altered in 'limbo()' via 'nonlocal y'.

        print(f"In {x}, starting to go deeper...")  # Indicating we're in Dream Level 2.
        dream_level_3()  # Going deeper into Dream Level 3.
        print(f"Back in {x}, after Dream Level 3.")  # Back in Dream Level 2, with 'x' possibly altered.
        # Please observe how 'x' may have changed due to the alterations made in Limbo.
        # In this code, 'x' in 'dream_level_2' was altered in 'limbo()' via 'nonlocal x'.

    print(f"In {x}, starting to go deeper...")  # Indicating we're in Dream Level 1.
    dream_level_2()  # Going deeper into Dream Level 2.
    print(f"Back in {x}, after Dream Level 2.")  # Back in Dream Level 1, 'x' remains unchanged here unless altered.
    # 'x' in 'dream_level_1' remains the same because we did not modify it.
    # This illustrates how variables at different levels are independent unless specifically altered.
    # Thanks for following along this journey through the dream levels.

print(f"In the {reality}, starting to dream...")  # Starting point in the Real World.
dream_level_1()  # Initiating the first level of the dream.
print(f"Back in the {reality}.")  # Back in the Real World after the dream sequence.
# Please notice how the 'reality' variable may have changed due to the 'global' keyword usage.
# Using 'global' allows us to alter the global state, much like how the characters' perceptions of reality are affected in "Inception".
# The global 'reality' variable was modified in 'limbo()', and the change persists even after all functions have completed.
# This is why we should use 'global' with care, as it can have far-reaching effects.

'''
What is nonlocal used for in this code and how does it affect variables?
Explanation:

In this code, nonlocal is used within the limbo function to modify variables (x and y) that are defined in the enclosing scopes (but not at the global level). Specifically:

nonlocal x inside limbo refers to the nearest enclosing x that is not in the global scope. In this case, it refers to x in dream_level_2.
nonlocal y refers to y in dream_level_3.
By declaring these variables as nonlocal, we can modify them within limbo, and these changes will persist in their respective scopes when we return from limbo. This mimics the idea in Inception of altering elements within a dream and having those changes affect the dreamer's perception when they return to higher levels.

'''

'''
What is global used for and how does it affect the variable reality?
Explanation:

global is used to indicate that we are referring to the global variable reality, not a local variable of the same name. Inside the limbo function:

global reality tells Python that any assignments to reality should modify the global variable, not create a new local variable.
By modifying reality in limbo, we are changing the global state of reality, which affects the program even after exiting all the nested functions.
This reflects the concept in Inception where altering the deepest subconscious levels can have profound effects on one's perception of reality upon waking up.

'''

'''
3. Why must we use global with care?
Explanation:

Using global must be done cautiously because:

Side Effects: Modifying global variables can lead to unexpected side effects that are hard to trace, especially in larger programs.
Debugging Difficulty: Changes to global state can make debugging more complex since any part of the code could potentially alter the global variable.
Maintainability: Relying on global variables can make the code less modular and harder to maintain.
In the context of the code and Inception, altering the global reality variable is akin to blurring the lines between dreams and reality, which can have dangerous consequences—much like the characters in the movie experience confusion between their dream states and the real world.
'''

'''
Please remember that nonlocal allows inner functions to modify variables in their enclosing (non-global) scopes, while global allows modification of variables at the global scope. Using these keywords can be powerful, but they should be used judiciously to maintain code clarity and prevent unintended side effects. Thanks for taking the time to delve into this explanation, and I hope it helps deepen your understanding of variable scopes in Python.
Please feel free to experiment with the code and observe how the use of nonlocal and global affects the variables at different scopes. Thanks again for your attention, and enjoy your journey through the layers of Python's variable scopes—much like traversing the dream levels in Inception!
At the start and end, we print the value of reality.
The change to reality made in limbo() affects the global state.
Highlights the caution needed when using global, as it impacts the entire program.
Thanks for your attention, and I hope this detailed explanation clarifies how nonlocal and global work.
'''