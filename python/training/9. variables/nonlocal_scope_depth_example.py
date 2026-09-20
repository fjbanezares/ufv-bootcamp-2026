# Let's explore nonlocal with a deep example where we have several levels of nested functions.
# We'll use many layers and demonstrate how nonlocal refers to the nearest enclosing scope. Thanks!

def level1():
    x1 = "x1 in level1"  # This is the outermost level's `x`

    def level2():
        x2 = "x2 in level2"  # This is `x` for level2
        
        def level3():
            x3 = "x3 in level3"  # `x` for level3, this won't be modified by nonlocal
            
            def level4():
                x4 = "x4 in level4"  # This is `x` for level4
                
                def level5():
                    nonlocal x4  # `x4` from level4 will be affected here
                    x4 = "modified x4 by nonlocal in level5"  # Change level4's `x`
                    print(f"In level5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                    # Please note that level1's x1, level2's x2, and level3's x3 are not affected.
                
                level5()  # Calling level5 from level4
                print(f"In level4 after level5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                # Please note x4 has changed in level4 because of the nonlocal reference in level5
            
            level4()  # Calling level4 from level3
            print(f"In level3 after level4: x1 = {x1}, x2 = {x2}, x3 = {x3}")
            # Please note x3 remains unchanged, since nonlocal only affected x4 in level4.
        
        level3()  # Calling level3 from level2
        print(f"In level2 after level3: x1 = {x1}, x2 = {x2}")
        # Please note x2 remains unchanged.

    level2()  # Calling level2 from level1
    print(f"In level1 after level2: x1 = {x1}")
    # Please note x1 remains unchanged.

# Let's run the full depth of function calls and see how nonlocal works.
level1()

print("\n--- Deeper nonlocal with multiple `x` at different levels ---\n")

# Let's dive even deeper into an example where multiple levels have a variable `x`
# and nonlocal affects the nearest `x`. We'll show which level's `x` is modified.

def deep_level1():
    x1 = "x1 in deep_level1"  # `x` at level 1

    def deep_level2():
        x2 = "x2 in deep_level2"  # `x` at level 2
        
        def deep_level3():
            x3 = "x3 in deep_level3"  # `x` at level 3
            
            def deep_level4():
                x4 = "x4 in deep_level4"  # `x` at level 4
                
                def deep_level5():
                    nonlocal x3  # Nonlocal will affect `x3` from level 3, NOT x4 or x2
                    x3 = "modified x3 by nonlocal in deep_level5"
                    print(f"In deep_level5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                    # x1, x2, and x4 are unaffected. Only x3 is modified!
                
                deep_level5()  # Calling level5 from level4
                print(f"In deep_level4 after deep_level5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                # Notice that x4 remains unchanged, but x3 was modified by level5.
            
            deep_level4()  # Calling level4 from level3
            print(f"In deep_level3 after deep_level4: x1 = {x1}, x2 = {x2}, x3 = {x3}")
            # x3 was modified, as it's the nearest `x` referenced by nonlocal in level5.
        
        deep_level3()  # Calling level3 from level2
        print(f"In deep_level2 after deep_level3: x1 = {x1}, x2 = {x2}")
        # x2 is not affected because nonlocal in level5 didn't reference x2.
    
    deep_level2()  # Calling level2 from level1
    print(f"In deep_level1 after deep_level2: x1 = {x1}")
    # x1 remains untouched.

# Running the deep example
deep_level1()

print("\n--- Let's make it even clearer by adding more layers ---\n")

def super_deep1():
    x1 = "Super x1 in super_deep1"  # Variable `x1` in level 1

    def super_deep2():
        x2 = "Super x2 in super_deep2"  # Variable `x2` in level 2
        
        def super_deep3():
            x3 = "Super x3 in super_deep3"  # Variable `x3` in level 3
            
            def super_deep4():
                x4 = "Super x4 in super_deep4"  # Variable `x4` in level 4
                
                def super_deep5():
                    nonlocal x4  # Modifying `x4` from level 4
                    x4 = "modified Super x4 by nonlocal in super_deep5"
                    print(f"In super_deep5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                    # Please note: x4 is modified but x1, x2, and x3 remain unchanged.
                
                super_deep5()  # Calling level5 from level4
                print(f"In super_deep4 after super_deep5: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
                # Please note x4 was changed in level4 due to nonlocal.

            super_deep4()  # Calling level4 from level3
            print(f"In super_deep3 after super_deep4: x1 = {x1}, x2 = {x2}, x3 = {x3}")
            # x3 remains untouched, even though x4 was modified.

        super_deep3()  # Calling level3 from level2
        print(f"In super_deep2 after super_deep3: x1 = {x1}, x2 = {x2}")
        # x2 remains untouched, only x4 was affected.

    super_deep2()  # Calling level2 from level1
    print(f"In super_deep1 after super_deep2: x1 = {x1}")
    # x1 remains untouched, only x4 was modified at the deepest level.

# Let's run this final deep example.
super_deep1()

# Now you have seen how nonlocal refers to the nearest enclosing scope and modifies that specific variable,
# while variables in higher levels or global scope remain unaffected.
# Thanks for going through the examples! Please keep practicing!
