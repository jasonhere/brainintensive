# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistIntensityMp2rageMasking


def test_JistIntensityMp2rageMasking_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inBackground=dict(argstr='--inBackground %s',
    ),
    inMasking=dict(argstr='--inMasking %s',
    ),
    inQuantitative=dict(argstr='--inQuantitative %s',
    ),
    inSecond=dict(argstr='--inSecond %s',
    ),
    inSkip=dict(argstr='--inSkip %s',
    ),
    inT1weighted=dict(argstr='--inT1weighted %s',
    ),
    null=dict(argstr='--null %s',
    ),
    outMasked=dict(argstr='--outMasked_T1_Map %s',
    hash_files=False,
    ),
    outMasked2=dict(argstr='--outMasked_T1weighted %s',
    hash_files=False,
    ),
    outSignal=dict(argstr='--outSignal_Proba %s',
    hash_files=False,
    ),
    outSignal2=dict(argstr='--outSignal_Mask %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    xDefaultMem=dict(argstr='-xDefaultMem %d',
    ),
    xMaxProcess=dict(argstr='-xMaxProcess %d',
    usedefault=True,
    ),
    xPrefExt=dict(argstr='--xPrefExt %s',
    ),
    )
    inputs = JistIntensityMp2rageMasking.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_JistIntensityMp2rageMasking_outputs():
    output_map = dict(outMasked=dict(),
    outMasked2=dict(),
    outSignal=dict(),
    outSignal2=dict(),
    )
    outputs = JistIntensityMp2rageMasking.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value