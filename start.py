from os import system
from rich import print

system("clear||cls")

print("[red on white]Welcome to your sailing expedition![/red on white]")

print("Today you will start your journey as the [bold cyan underline]sailor[/bold cyan underline] of this trip. This trip will be the trip of your life")
print("")
print("You've been sailing for a while and one of your crew comes up and says captain can we make a quick detour I wanna pick up some supplies at the nearby island?")
print("1. listen to the crewmate and make the detour")
print("2. continue on the planned route")

choice = input("Make a choice!:")
if choice== "1":
    print("you've made the detour and now have extra supplies and surpirsingly they had enough supplies there so yo uwere in and out real quick")
    print("a few months pass and your now passing through the strait")
    print("as you pass through the strait you see a around hundred people all on small boats pull up to your ship asking to get on saying their the newly instated patrol in the strait")
    print("1. let them on the ship I don't wanna get in trouble with the police")
    print("2. decide that it's too suspicious and refuse the let them on")
    choice = input("Make a choice!:")
    if choice == "1":
        print("As you let them on the ship they turn out to be pirates taking over your ship to harass people going through the strait and you end up dying. end 5")
    elif choice == "2":
        print("As you refuse to let them on, you see them annoyed, but they eventually turn around and you continue onwards.")
        print("you continue sailing on the planned route for another few months, you hear at some point that you were quite lucky and just about a month after you left a huge storm appeared on the place you passed")
        print("At this point in the trip you've gotten far enough that more investors have appeared and at your next resupply one the investors is there with a brand new luxury ship very heavily branded and asks you to replace your ship with the new luxury branded one")
        print("As your inspecting the new branded ship you see that is has seems to have been hastily put together, but it should probably be fine")
        print("1. listen to the investor and take the new branded ship")
        print("2. decide against it losing an investment oppurtunity and money for supplies along with the new ship")
        choice = input("Make a choice!:")
        if choice== "1":
            print("you decide to take the new ship but about a month later the flaws and mistakes in the sip become more and more noticable, and cracks start appearing and eventually your ship sinks and you die. end 6")
        elif choice== "2":
            print("You decide against using the hastily put together ship and continue on your journey")
            print("your finally on the last leg of your expedition, but there is just one final decision to make, you can either pass through a section of the arctic speeding up the expedition tremendously, or go the long route and finish the expedition as planned")
            print("1. go through the arctic, it's much faster and very cool")
            print("2. It's best to avoid the arctic, it could get too cold and is unplanned")
            choice = input("Make a choice!:")
            if choice== "1":
                print("As you go through the arctic the fog gets horrendously bad and you end up hitting an iceberg, stranding you for months eventually you starve. end 7")
            elif choice== "2":
                print("you decide to avoid unplanned detours, but the fog gets really bad, however luckily there nothing out in the ocean so you're fine and you finish the expedition of a lifetime and the investments and sponsorhips you gained from this has let you retire early and live out your life happy. Good end, 8")
elif choice== "2":
    print("No I don't think we should we have a set path and if we detour the weather may get worse")
    print("2 months later you find yourself at in impasse you can either make a one month detour or go through the strait which was rumored to have recently been taken by pirates")
    print("What do you want to do next?")
    print("1. decide it'd be more dangerous to stray off the path and go into the strait")
    print("2. take the long unplanned detour")
    choice = input("Make a choice!:")

    if choice== "1":
        print("as you drive through the strait you encounter a group of pirates who've taken over another ship and they ask for all of your supplies or they blow you to hell")
        print("1. give them the supplies, its better than dying")
        print("2. Try an fight back we starve if we lose these supplies")
        choice = input("Make a choice!:")

        if choice== "1":
            print("you give them the supplies and they actually let you through however without any supplies you have to end the expedition early and now with and now your dreams and aspirations are over but at least your alive (end 1)")
            
        elif choice== "2":
            print("as you refuse to hand over your supples true to their word the pirates blow your ship to smithereans adn you die to an explosion while watching your ship sink (end 2)")

    elif choice== "2":
        print("you decide its better to take the detour instead of risking your life goign through the strait")
        print("your running low on supplies and your not sure if you're not sure if you'll have enough for the trip")
        print("you can either keep going hoping theres enough or you can stop at sandanelpha for supplies however your not sure if this will take too long as if you do it may cause the weather to be too unfavorable later on")
        print("1. keep on going")
        print("2. stop for a restock")
        choice = input("make a choice:")
        if choice== "1":
            print("you decide to continue onwards without getting more supplies however later on you get caught up in a storm taking you off route and as you try to get back to land you run out of food, and slowly, painfully all of your crew and yourself starve. end 3")
        
        elif choice== "2":
            print("You take the detour and get some supplies, but it takes longer than you'd hoped as this place doesn't have all the supplies you need immediately so you have to wait for it to arrive, but just like you thought the weather turns incredibly cold and some of the crew unprepared for the cold succumb to frostbite and once you finally reach land you have to end the expedition as youve lost much of the crew. end 4")