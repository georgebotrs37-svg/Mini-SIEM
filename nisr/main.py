from pathlib import Path

try:
    from .core.watcher import follow
    from .core.detector import analyze
    from .core.alert import send
    from .state.tracker import is_new
    from .config import LOG_FILE
except ImportError:
    from core.watcher import follow
    from core.detector import analyze
    from core.alert import send
    from state.tracker import is_new
    from config import LOG_FILE

from PIL import Image


def show_image(path):
    candidates = [
        Path(path),
        Path(__file__).resolve().parent.parent / path,
        Path(__file__).resolve().parent / path,
    ]

    for candidate in candidates:
        if not candidate.exists():
            continue
        try:
            img = Image.open(candidate)
            img.show()
            return
        except Exception as e:
            print(f"Image error: {e}")
            return

    return


def print_alert(alert):
    print("\n==============================")
    print(f"[{alert['severity']}] {alert['type']}")

    if "user" in alert:
        print(f"User: {alert['user']}")

    if "ip" in alert:
        print(f"IP: {alert['ip']}")

    print(f"Log: {alert['raw']}")
    print("==============================\n")


def main():
    print("NISR Started")

    show_image("logo.png.jpg")

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as logfile:
            loglines = follow(logfile)

            for line in loglines:
                alert = analyze(line)

                if alert and is_new(alert):
                    print_alert(alert)
                    show_image("alert.png.jpg")
                    send(alert)

    except FileNotFoundError:
        print(f"Log file not found: {LOG_FILE}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()