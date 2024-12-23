import psutil
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
import platform

console = Console()

def get_cpu_usage(interval: float = 1.0) -> float:
    """Fetch the overall CPU usage percentage."""
    return psutil.cpu_percent(interval=interval)

def get_per_core_usage(interval: float = 1.0) -> list:
    """Fetch the CPU usage percentage for each core."""
    return psutil.cpu_percent(interval=interval, percpu=True)

def get_cpu_info():
    """Get detailed CPU information."""
    cpu_info = {}
    # Basic CPU Information
    cpu_info['processor'] = platform.processor()
    cpu_info['architecture'] = platform.machine()
    cpu_info['physical_cores'] = psutil.cpu_count(logical=False)
    cpu_info['total_cores'] = psutil.cpu_count(logical=True)
    
    # CPU Frequency Information
    cpu_freq = psutil.cpu_freq()
    cpu_info['max_frequency'] = cpu_freq.max if cpu_freq else "N/A"
    cpu_info['min_frequency'] = cpu_freq.min if cpu_freq else "N/A"
    cpu_info['current_frequency'] = cpu_freq.current if cpu_freq else "N/A"
    
    # CPU Stats
    cpu_stats = psutil.cpu_stats()
    cpu_info['ctx_switches'] = cpu_stats.ctx_switches
    cpu_info['interrupts'] = cpu_stats.interrupts
    cpu_info['soft_interrupts'] = cpu_stats.soft_interrupts
    cpu_info['syscalls'] = cpu_stats.syscalls
    
    # CPU Times
    cpu_times = psutil.cpu_times()
    cpu_info['user_time'] = cpu_times.user
    cpu_info['system_time'] = cpu_times.system
    cpu_info['idle_time'] = cpu_times.idle
    
    # Load Average
    try:
        load1, load5, load15 = psutil.getloadavg()
        cpu_info['load_avg'] = {'1min': load1, '5min': load5, '15min': load15}
    except:
        cpu_info['load_avg'] = {'1min': "N/A", '5min': "N/A", '15min': "N/A"}
    
    return cpu_info

def display_cpu_usage():
    """Display CPU usage with a progress bar and per-core usage table."""
    overall_usage = get_cpu_usage()
    per_core_usage = get_per_core_usage()

    with Progress(
        TextColumn("[bold cyan]Overall CPU Usage"),
        BarColumn(bar_width=40, style="bold green"),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("CPU Usage", total=100)
        progress.update(task, completed=overall_usage)
        progress.refresh()

    table = Table(title="Per-Core CPU Usage", show_header=True, header_style="bold magenta")
    table.add_column("Core", style="dim", width=6)
    table.add_column("Usage (%)", justify="right")

    for idx, usage in enumerate(per_core_usage, start=1):
        table.add_row(f"Core {idx}", f"{usage}%")

    panel = Panel(table, title="CPU Cores", border_style="green")
    console.print(panel)

def display_cpu_info():
    """Display comprehensive CPU information."""
    cpu_info = get_cpu_info()
    
    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    
    # Basic CPU Information Table
    basic_table = Table(title="CPU Basic Information", show_header=True, header_style="bold magenta")
    basic_table.add_column("Property", style="cyan")
    basic_table.add_column("Value", style="green")
    
    basic_table.add_row("Processor", str(cpu_info['processor']))
    basic_table.add_row("Architecture", str(cpu_info['architecture']))
    basic_table.add_row("Physical Cores", str(cpu_info['physical_cores']))
    basic_table.add_row("Total Cores (with HT)", str(cpu_info['total_cores']))
    
    # Frequency Information Table
    freq_table = Table(title="CPU Frequency Information", show_header=True, header_style="bold magenta")
    freq_table.add_column("Property", style="cyan")
    freq_table.add_column("Value", style="green")
    
    freq_table.add_row("Maximum Frequency", f"{cpu_info['max_frequency']:.2f} MHz" if cpu_info['max_frequency'] != "N/A" else "N/A")
    freq_table.add_row("Minimum Frequency", f"{cpu_info['min_frequency']:.2f} MHz" if cpu_info['min_frequency'] != "N/A" else "N/A")
    freq_table.add_row("Current Frequency", f"{cpu_info['current_frequency']:.2f} MHz" if cpu_info['current_frequency'] != "N/A" else "N/A")
    
    # CPU Statistics Table
    stats_table = Table(title="CPU Statistics", show_header=True, header_style="bold magenta")
    stats_table.add_column("Property", style="cyan")
    stats_table.add_column("Value", style="green")
    
    stats_table.add_row("Context Switches", f"{cpu_info['ctx_switches']:,}")
    stats_table.add_row("Interrupts", f"{cpu_info['interrupts']:,}")
    stats_table.add_row("Soft Interrupts", f"{cpu_info['soft_interrupts']:,}")
    stats_table.add_row("System Calls", f"{cpu_info['syscalls']:,}")
    
    # CPU Times Table
    times_table = Table(title="CPU Times", show_header=True, header_style="bold magenta")
    times_table.add_column("Property", style="cyan")
    times_table.add_column("Value (seconds)", style="green")
    
    times_table.add_row("User Time", f"{cpu_info['user_time']:.2f}")
    times_table.add_row("System Time", f"{cpu_info['system_time']:.2f}")
    times_table.add_row("Idle Time", f"{cpu_info['idle_time']:.2f}")
    
    # Load Average Table
    load_table = Table(title="Load Average", show_header=True, header_style="bold magenta")
    load_table.add_column("Time Span", style="cyan")
    load_table.add_column("Value", style="green")
    
    load_table.add_row("1 minute", f"{cpu_info['load_avg']['1min']:.2f}" if isinstance(cpu_info['load_avg']['1min'], float) else "N/A")
    load_table.add_row("5 minutes", f"{cpu_info['load_avg']['5min']:.2f}" if isinstance(cpu_info['load_avg']['5min'], float) else "N/A")
    load_table.add_row("15 minutes", f"{cpu_info['load_avg']['15min']:.2f}" if isinstance(cpu_info['load_avg']['15min'], float) else "N/A")
    
    # Create panels for each section
    basic_panel = Panel(basic_table, title="Basic Information", border_style="blue")
    freq_panel = Panel(freq_table, title="Frequency Details", border_style="green")
    stats_panel = Panel(stats_table, title="Statistics", border_style="yellow")
    times_panel = Panel(times_table, title="CPU Times", border_style="red")
    load_panel = Panel(load_table, title="Load Average", border_style="magenta")
    
    # Print all panels with some spacing
    console.print("\n")
    console.print(basic_panel)
    console.print("\n")
    console.print(freq_panel)
    console.print("\n")
    console.print(stats_panel)
    console.print("\n")
    console.print(times_panel)
    console.print("\n")
    console.print(load_panel)