## basic job configuration
import AthenaCommon.AtlasUnixStandardJob
 
#--------------------------------------------------------------
# Event related parameters
#--------------------------------------------------------------
from AthenaCommon.AppMgr import ToolSvc,theApp,ServiceMgr
theApp.EvtMax = 300
 
import AthenaPoolCnvSvc.ReadAthenaPool
 
#ServiceMgr.EventSelector.InputCollections = ['root://fax.mwt2.org:1094//pnfs/uchicago.edu/atlaslocalgroupdisk/rucio/user/ivukotic/1b/32/test_file1.root']
#ServiceMgr.EventSelector.InputCollections = ['root://dcdoor11.usatlas.bnl.gov:1094//pnfs/usatlas.bnl.gov/LOCALGROUPDISK/rucio/user/ivukotic/1b/32/test_file1.root']
#ServiceMgr.EventSelector.InputCollections = ['root://grid05.lal.in2p3.fr:1094//dpm/lal.in2p3.fr/home/atlas/atlasscratchdisk/rucio/user/ivukotic/1b/32/test_file1.root']
ServiceMgr.EventSelector.InputCollections = ['http://test-gsoc.web.cern.ch/test-gsoc/DAOD_EGAM5.11352290._000183.pool.root.1']
#ServiceMgr.EventSelector.InputCollections = ['/build1/xAOD/mc16_13TeV/DAOD_EGAM5.11352290._000183.pool.root.1']

# Reading Parameters
ServiceMgr.AthenaPoolCnvSvc.InputPoolAttributes += [ "ContainerName = 'CollectionTree'; TREE_CACHE = '-1'" ]
ServiceMgr.AthenaPoolCnvSvc.InputPoolAttributes += [ "TREE_CACHE_LEARN_EVENTS = '100'" ]
ServiceMgr.AthenaPoolCnvSvc.PrintInputAttrPerEvt += [ "FILE_READ_CALLS = 'int'" ]

ServiceMgr.AthenaPoolCnvSvc.InputPoolAttributes += [ "ASYNC_PREFETCHING = '1'" ]

ServiceMgr.AthenaPoolCnvSvc.UseDetailChronoStat = True
ServiceMgr.AthenaPoolCnvSvc.SkipFirstChronoCommit = True
 
# Copy Output
from AthenaPoolCnvSvc.WriteAthenaPool import AthenaPoolOutputStream
StreamAOD = AthenaPoolOutputStream( "StreamAOD" , "AOD_copy.pool.root" , True )
# Base the xAOD branch names just on the SG keys:
StreamAOD.WritingTool.SubLevelBranchName = "<key>"
 
StreamAOD.ForceRead = True
StreamAOD.TakeItemsFromInput = True
StreamAOD.ExcludeList += [ "CaloCellContainer#*" ]
StreamAOD.ExcludeList += [ "TileCellContainer#*" ]
StreamAOD.ExcludeList += [ "CaloClusterCellLinkContainer#*" ]
 
#--------------------------------------------------------------
# Performance Monitoring
#--------------------------------------------------------------
from PerfMonComps.PerfMonFlags import jobproperties as pmjp
pmjp.PerfMonFlags.doPostProcessing = True
pmjp.PerfMonFlags.doSemiDetailedMonitoringFullPrint = True
#pmjp.PerfMonFlags.doDetailedMonitoring = True
 
#--------------------------------------------------------------
# Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL)
#--------------------------------------------------------------
ServiceMgr.MessageSvc.OutputLevel = 3
ServiceMgr.MessageSvc.defaultLimit = 10000000
ServiceMgr.ChronoStatSvc.PrintEllapsedTime = True
 
#
# End of job options file
#
###############################################################
 
