# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..converters import DicomToNrrdConverter


def test_DicomToNrrdConverter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputDicomDirectory=dict(argstr='--inputDicomDirectory %s',
    ),
    outputDirectory=dict(argstr='--outputDirectory %s',
    hash_files=False,
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    ),
    smallGradientThreshold=dict(argstr='--smallGradientThreshold %f',
    ),
    terminal_output=dict(nohash=True,
    ),
    useBMatrixGradientDirections=dict(argstr='--useBMatrixGradientDirections ',
    ),
    useIdentityMeaseurementFrame=dict(argstr='--useIdentityMeaseurementFrame ',
    ),
    writeProtocolGradientsFile=dict(argstr='--writeProtocolGradientsFile ',
    ),
    )
    inputs = DicomToNrrdConverter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DicomToNrrdConverter_outputs():
    output_map = dict(outputDirectory=dict(),
    )
    outputs = DicomToNrrdConverter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value