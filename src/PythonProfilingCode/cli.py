"""Console script for PythonProfilingCode."""

import typer
import psutil
from rich.console import Console
from src.modules.profilingCode.concatenation.avoidlistcomprehensioniniterationsbad import avoidlistcomprehensioniniterationsbad
from src.modules.profilingCode.concatenation.avoidlistcomprehensioniniterationsgood import avoidlistcomprehensioniniterationsgood
from src.modules.profilingCode.concatenation.avoiddoublequotecheckbad import avoiddoublequotecheckbad
from src.modules.profilingCode.concatenation.avoiddoublequotecheckgood import avoiddoublequotecheckgood

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for PythonProfilingCode."""
    """Algorithm servermanufgwp(kgCO2eq) = servertypegwp(kgCO2eq) + cpuunits(unit) x cpubasegwp(kgCO2eq/unit) + ramsize(GB) x ramsizegwp(kgCO2eq/GB)"""
    """MacBook M2 benchmarks"""
    servertypegwp = 147
    cpubasegwp = 150
    ramsizegwp = 3

    """Execution and calculation of bad code practice"""
    avoidlistcomprehensioniniterationsbad(100000000)
    cpuunits = psutil.cpu_percent(1)
    ramsize = psutil.swap_memory().used
    servermanufgwp = servertypegwp + cpuunits * cpubasegwp + ramsize * ramsizegwp
    console.print(servermanufgwp)

    """Execution and calculation of good code practice"""
    avoidlistcomprehensioniniterationsgood(100000000)
    cpuunits = psutil.cpu_percent(1)
    ramsize = psutil.swap_memory().used
    servermanufgwp = servertypegwp + cpuunits * cpubasegwp + ramsize * ramsizegwp
    console.print(servermanufgwp)

    """Execution and calculation of bad code practice"""
    avoiddoublequotecheckbad(100000000)
    cpuunits = psutil.cpu_percent(1)
    ramsize = psutil.swap_memory().used
    servermanufgwp = servertypegwp + cpuunits * cpubasegwp + ramsize * ramsizegwp
    console.print(servermanufgwp)

    """Execution and calculation of good code practice"""
    avoiddoublequotecheckgood(100000000)
    cpuunits = psutil.cpu_percent(1)
    ramsize = psutil.swap_memory().used
    servermanufgwp = servertypegwp + cpuunits * cpubasegwp + ramsize * ramsizegwp
    console.print(servermanufgwp)


if __name__ == "__main__":
    typer.run(main)
