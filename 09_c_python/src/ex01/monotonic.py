import ctypes


def monotonic():
    if hasattr(ctypes, 'windll') and hasattr(ctypes.windll.kernel32, 'GetTickCount64'):
        # Windows
        # convert milliseconds to seconds
        return ctypes.windll.kernel32.GetTickCount64() / 1000

    if hasattr(ctypes, 'cdll') and hasattr(ctypes.cdll.LoadLibrary(None), 'clock_gettime'):
        # Unix-based systems (e.g., Linux, MacOS)
        CLOCK_MONOTONIC_RAW = 4  # constant for monotonic raw clock

        # Define the function signature
        libc = ctypes.cdll.LoadLibrary(None)
        libc.clock_gettime.argtypes = [
            ctypes.c_int, ctypes.POINTER(ctypes.c_long)]
        libc.clock_gettime.restype = ctypes.c_int

        # Call the function and return the result
        timespec = ctypes.c_long()
        libc.clock_gettime(CLOCK_MONOTONIC_RAW, ctypes.byref(timespec))
        return timespec.value

    raise NotImplementedError(
        "Monotonic clock function not available for this operating system")


if __name__ == "__main__":
    print(monotonic())
