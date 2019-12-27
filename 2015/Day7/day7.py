inputs = [s.strip().split('->')
          for s in open('input.txt').read().splitlines()]

circuit = {}
for signal, output_wire in inputs:
    circuit[output_wire.strip()] = signal.strip()

output_wire = 'c'
for _ in range(100):
    signal = circuit.get(output_wire)
    signal = str(signal)
    if 'AND' in signal:
        wires = signal.split('AND')
        signal_value = circuit.get(wires[0]) & circuit.get(wires[1])
    elif 'OR' in signal:
        wires = signal.split('OR')
        signal_value = circuit.get(wires[0]) | circuit.get(wires[1])
    elif 'LSHIFT' in signal:
        wire, shift_ammount = signal.split('LSHIFT')
        signal_value = circuit.get(wire) << int(shift_ammount)
    elif 'RSHIFT' in signal:
        wire, shift_ammount = signal.split('RSHIFT')
        signal_value = circuit.get(wire) >> int(shift_ammount)
    elif 'NOT' in signal:
        wire = signal.split('NOT')[1]
        signal_value = circuit.get(wire) ^ 65535
    else:
        signal_value = int(signal)
    circuit[output_wire] = signal_value
    if isinstance(circuit.get('a'),int):
        break  

print(circuit)
