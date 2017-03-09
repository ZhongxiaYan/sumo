# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, False)

# apply zoom
netedit.zoomIn(match.getTarget().offset(325, 100), 10)

# select E3
netedit.changeAdditional("e3Detector")

# create E3
netedit.leftClick(match, 250, 400)

# select entry detector
netedit.changeAdditional("detEntry")

# Create Entry detector E3
netedit.selectAdditionalChild(4, 0)
netedit.leftClick(match, 200, 180)

# go to inspect mode
netedit.inspectMode()

# inspect Entry
netedit.leftClick(match, 250, 180)

# Change parameter 0 with a non valid value (dummy Lane)
netedit.modifyAttribute(0, "dummyLane")

# Change parameter 0 with a non valid value (Empty lane)
netedit.modifyAttribute(0, "")

# Change parameter 0 with a valid value (other lane)
netedit.modifyAttribute(0, "gneE3_0")

# Change parameter 1 with a non valid value (dummy position X)
netedit.modifyAttribute(1, "dummy position")

# Change parameter 1 with a non valid value (empty)
netedit.modifyAttribute(1, "")

# Change parameter 1 with a valid value (different position X)
netedit.modifyAttribute(1, "25")

# go to a empty area
netedit.leftClick(match, 0, 0)

# Check undos and redos
netedit.undo(match, 4)
netedit.redo(match, 4)

# save additionals
netedit.saveAdditionals()

# save newtork
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess, False, False)
