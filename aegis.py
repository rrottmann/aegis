import sys
import logging
import secrets
import string

pinpad = {
    "a": 2,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 3,
    "f": 3,
    "g": 4,
    "h": 4,
    "i": 4,
    "j": 5,
    "k": 5,
    "l": 5,
    "m": 6,
    "n": 6,
    "o": 6,
    "p": 7,
    "q": 7,
    "r": 7,
    "s": 7,
    "t": 8,
    "u": 8,
    "v": 8,
    "w": 9,
    "x": 9,
    "y": 9,
    "z": 9,
}


def password2pincode(password=None, length=16):
    if password is None:
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for i in range(length)).lower()
    password = password.lower()
    if len(password) > 16:
        logging.error("Invalid length. Must be less than 16 digits.")
        sys.exit(1)
    if len(password) < 7:
        logging.error("Invalid length. Must be more than 16 digits.")
        sys.exit(1)
    pincode = ""
    for _ in password:
        pincode = pincode + str(pinpad[_])
    return password, pincode


def complete_reset():
    print("== Complete Reset ==")
    print("Press LOCK + UNLOCK + 2 for 10 seconds")
    print("> RED and BLUE LED blink alternately")
    print("> GREEN and BLUE LED glow solidly when successful")


def set_admin_pin(length=10):
    print("== Set Admin PIN ==")
    print("Press UNLOCK")
    print("> GREEN and BLUE LED glow solidly")
    print("Press UNLOCK + 9")
    print("> WHILE BLUE LED glows solidly, GREEN LED blinks")
    admin_password, admin_pincode = password2pincode(length=length)
    print(f"# {admin_password}")
    print(f"Press {' + '.join([x for x in admin_pincode])}")
    print("Press UNLOCK")
    print(f"Press {' + '.join([x for x in admin_pincode])}")
    print("> GREEN LED will illuminate 1 second and BLUE LED will be solid")
    print("PRESS LOCK to exit Admin Mode")
    print("== Enter Admin Mode ==")
    print("Press UNLOCK + 0 for five seconds")
    print("> RED LED blinks")
    print(f"Press {' + '.join([x for x in admin_pincode])}")
    print("Press UNLOCK")
    print("> BLUE LED solid")
    return admin_password, admin_pincode


def set_user_pin(length=10):
    print("== Set User PIN ==")
    print("Press UNLOCK + 1 until BLUE LED is solid and GREEN LED blinks")
    password, pincode = password2pincode(length=10)
    print(f"# {password}")
    print(f"Press {' + '.join([x for x in pincode])}")
    print("Press UNLOCK")
    print(f"> GREEN LED blinks three times")
    print(f"Press {' + '.join([x for x in pincode])}")
    print("Press UNLOCK")
    print("> BLUE LED solid")

    return password, pincode


def set_recover_code(num=4, length=10):
    # a maximum of 4 one-time recover codes can be set
    if num > 4:
        num = 4
    if num <= 0:
        return
    for _ in range(num + 1):
        print(f"== Set One-Time-Use Recovery PIN {_} ==")
        print("Press UNLOCK + 8 until BLUE LED is solid and GREEN LED blinks three times")
        recover_password, recover_pincode = password2pincode(length=length)
        print(f"# {recover_password}")
        print(f"Press {' + '.join([x for x in recover_pincode])}")
        print("Press UNLOCK")
        print(f"> GREEN LED blinks three times")
        print(f"Press {' + '.join([x for x in recover_pincode])}")
        print("Press UNLOCK")
        print("> GREEN LED blinks three times then BLUE LED solid")


def exit_admin_mode():
    print("PRESS LOCK to exit Admin Mode")


def enter_admin_mode(admin_pincode):
    print("== Enter Admin Mode ==")
    print("Press UNLOCK + 0 for five seconds")
    print("> RED LED blinks")
    print(f"Press {' + '.join([x for x in admin_pincode])}")
    print("Press UNLOCK")
    print("> BLUE LED solid")


def set_destruct_code(length=10):
    print("== Set Destruct PIN ==")
    print("Press 7 + 4 until GREEN LED blinks three times")
    print("Press UNLOCK + 3 until RED LED and BLUE LED blink alternately")
    destroy_password, destroy_pincode = password2pincode(length=length)
    print(f"# {destroy_password}")
    print(f"Press {' + '.join([x for x in destroy_pincode])}")
    print("Press UNLOCK")
    print(f"> GREEN LED blinks three times")
    print(f"Press {' + '.join([x for x in destroy_pincode])}")
    print("Press UNLOCK")
    print("> BLUE LED solid")


if __name__ == "__main__":
    print('=' * 80)
    print('=== APRICORN AEGIS SETUP PROCEDURE ===')
    print('=' * 80)
    complete_reset()
    print('-' * 80)
    admin_password, admin_pincode = set_admin_pin(length=10)
    user_password, user_pincode = set_user_pin(length=10)
    exit_admin_mode()
    print('-' * 80)
    enter_admin_mode(admin_pincode=admin_pincode)
    set_recover_code(num=4, length=16)
    exit_admin_mode()
    print('-' * 80)
    enter_admin_mode(admin_pincode=admin_pincode)
    set_destruct_code(length=10)
    exit_admin_mode()
    print('-' * 80)
