def initialize_course_master_data():
    # Simulating master data tables of course rooms (similar to static data in banking systems)
    course_room_map = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    course_instructor_map = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    course_schedule_map = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    return course_room_map, course_instructor_map, course_schedule_map

def get_course_details(course_code, room_map, instructor_map, schedule_map):
    # Lookup function (similar to reference data lookup in banking systems)
    if course_code in room_map:
        return {
            "room": room_map[course_code],
            "instructor": instructor_map[course_code],
            "schedule": schedule_map[course_code]
        }
    else:
        return None

def process_user_request():
    room_map, instructor_map, schedule_map = initialize_course_master_data()

    try:
        course_code = input("Enter course code (such as CSC101): ").upper().strip()

        course_info = get_course_details(
            course_code,
            room_map,
            instructor_map,
            schedule_map
        )

        if course_info:
            print("\n#### Course Information ####")
            print(f"Room Number   : {course_info['room']}")
            print(f"Instructor    : {course_info['instructor']}")
            print(f"Meeting Time  : {course_info['schedule']}")
        else:
            print("Course not found. Please verify the course code.")

    except Exception as error:
        print("System error occurred during request processing:", error)

def main():
    print("#### University Course Lookup System ####")
    process_user_request()

if __name__ == "__main__":
    main()
