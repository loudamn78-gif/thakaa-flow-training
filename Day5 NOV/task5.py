# لعبة الهبوط على القمر

GRAVITY = 1.62


def step(altitude, velocity, fuel, thrust):
    new_velocity = velocity + GRAVITY - (thrust * 0.5)
    new_altitude = altitude - new_velocity
    new_fuel = fuel - thrust
    return new_altitude, new_velocity, new_fuel


def autopilot(altitude, velocity, fuel):
    # خليت المركبة تنزل في البداية بدون دفع لتوفير الوقود.
    # إذا اقتربت من السطح وكانت السرعة عالية أشغل الدفع الكامل.
    # وقبل الهبوط أخفف السرعة بحيث تكون آمنة عند الوصول للقمر.

    thrust = 0

    if velocity > 2:
        steps_to_stop = (velocity - 2) / 3.38
        stop_distance = steps_to_stop * (velocity + 2) / 2

        if altitude <= stop_distance + velocity + 3:
            thrust = 10

    elif altitude < 30:
        thrust = (velocity + GRAVITY - 2) / 0.5

    if thrust < 0:
        thrust = 0

    if thrust > 10:
        thrust = 10

    thrust = int(round(thrust))

    if thrust > fuel:
        thrust = int(fuel)

    return thrust


def ask_thrust(fuel):
    while True:
        text = input("Thrust (0-10): ")

        if not text.isdigit():
            print("Please enter a number.")
            continue

        thrust = int(text)

        if thrust > 10:
            print("Thrust must be 10 or less.")
        elif thrust > fuel:
            print("Not enough fuel.")
        else:
            return thrust


def play(use_autopilot):
    altitude = 1000
    velocity = 0
    fuel = 200
    time = 0

    while altitude > 0:
        print(
            f"t={time}s | altitude: {altitude:.1f} m | speed: {velocity:.1f} m/s | fuel: {fuel}"
        )

        if use_autopilot:
            thrust = autopilot(altitude, velocity, fuel)
            print("Thrust (0-10):", thrust)
        else:
            thrust = ask_thrust(fuel)

        altitude, velocity, fuel = step(
            altitude,
            velocity,
            fuel,
            thrust
        )

        time += 1

    if velocity <= 3:
        print(
            f"Safe landing at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {time} s"
        )
    else:
        print(
            f"Crashed at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {time} s"
        )


mode = input("Manual (m) or Autopilot (a)? ")
play(mode.lower() == "a")