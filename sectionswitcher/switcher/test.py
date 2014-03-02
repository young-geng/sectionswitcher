import re
import json

text = """{
 "ClassOffering": {
  "classUID": "STAT.2.Spring.2014",
  "courseNumber": 2,
  "courseTitle": "Introduction to Statistics",
  "courseUID": "STAT.2",
  "departmentCode": "STAT",
  "lowerUnits": 4,
  "sectionUID": "STAT.2.Spring.2014.001",
  "sections": [
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LEC",
    "sectionId": "STAT.2.001",
    "sectionMeetings": {
     "building": "HAAS",
     "endTime": "1100 AM",
     "instructorNames": "D'ABRERA, H M",
     "meetingDay": "  T T",
     "room": " F0295",
     "startTime": "0930"
    },
    "sectionNumber": "001",
    "sectionType": "PRIMARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/001",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LEC",
    "sectionId": "STAT.2.002",
    "sectionMeetings": {
     "building": "LEWIS",
     "endTime": "1100 AM",
     "instructorNames": "IBSER, F H",
     "meetingDay": " M W F",
     "room": "0100",
     "startTime": 1000
    },
    "sectionNumber": "002",
    "sectionType": "PRIMARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/002",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.101",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "1000 AM",
     "instructorNames": "COMEAUX, A C",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": "0900"
    },
    "sectionNumber": 101,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/101",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.102",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "1000 AM",
     "instructorNames": "KIM, A",
     "meetingDay": " M W",
     "room": "0334",
     "startTime": "0900"
    },
    "sectionNumber": 102,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/102",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.103",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "1100 AM",
     "instructorNames": "TOTH, B K",
     "meetingDay": " M W",
     "room": "0334",
     "startTime": 1000
    },
    "sectionNumber": 103,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/103",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.104",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "1100 AM",
     "instructorNames": "COMEAUX, A C",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": 1000
    },
    "sectionNumber": 104,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/104",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.105",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "1200 PM",
     "instructorNames": "TOTH, B K",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": 1100
    },
    "sectionNumber": 105,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/105",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.106",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0100 PM",
     "instructorNames": "KIM, A",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": 1200
    },
    "sectionNumber": 106,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/106",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.107",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0200 PM",
     "instructorNames": "KARTHIKEYAN, D",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": "0100"
    },
    "sectionNumber": 107,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/107",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.108",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0200 PM",
     "instructorNames": "GAYAM, A R",
     "meetingDay": " M W",
     "room": "0344",
     "startTime": "0100"
    },
    "sectionNumber": 108,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/108",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.109",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0300 PM",
     "instructorNames": "KARTHIKEYAN, D",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": "0200"
    },
    "sectionNumber": 109,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/109",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.110",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0300 PM",
     "instructorNames": "SHERMAN, Z M",
     "meetingDay": " M W",
     "room": "0332",
     "startTime": "0200"
    },
    "sectionNumber": 110,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/110",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.111",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0400 PM",
     "instructorNames": "SHERMAN, Z M",
     "meetingDay": " M W",
     "room": "0330",
     "startTime": "0300"
    },
    "sectionNumber": 111,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/111",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.112",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0500 PM",
     "instructorNames": "GAYAM, A R",
     "meetingDay": " M W",
     "room": "0081",
     "startTime": "0400"
    },
    "sectionNumber": 112,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/112",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.201",
    "sectionMeetings": {
     "building": "LATIMER",
     "endTime": "0100 PM",
     "instructorNames": "CHEN, C",
     "meetingDay": " M W",
     "room": "0122",
     "startTime": 1200
    },
    "sectionNumber": 201,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/201",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.202",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0100 PM",
     "instructorNames": "MUKHOPADHYAY, S",
     "meetingDay": " M W",
     "room": "0047",
     "startTime": 1200
    },
    "sectionNumber": 202,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/202",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.203",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0200 PM",
     "instructorNames": "MUKHOPADHYAY, S",
     "meetingDay": " M W",
     "room": "0047",
     "startTime": "0100"
    },
    "sectionNumber": 203,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/203",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.204",
    "sectionMeetings": {
     "building": "LATIMER",
     "endTime": "0200 PM",
     "instructorNames": "CHEN, C",
     "meetingDay": " M W",
     "room": "0122",
     "startTime": "0100"
    },
    "sectionNumber": 204,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/204",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.205",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0300 PM",
     "instructorNames": "CATTELL, L",
     "meetingDay": " M W",
     "room": "0045",
     "startTime": "0200"
    },
    "sectionNumber": 205,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/205",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.206",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0300 PM",
     "instructorNames": "NORGREN, M S",
     "meetingDay": " M W",
     "room": "0047",
     "startTime": "0200"
    },
    "sectionNumber": 206,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/206",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.207",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0400 PM",
     "meetingDay": " M W",
     "room": "0041",
     "startTime": "0300"
    },
    "sectionNumber": 207,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/207",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.208",
    "sectionNumber": 208,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/208",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.209",
    "sectionNumber": 209,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/209",
    "waitlistSize": 0
   },
   {
    "seatLimit": 0,
    "seatsAvailable": 0,
    "sectionFormat": "LAB",
    "sectionId": "STAT.2.210",
    "sectionMeetings": {
     "building": "EVANS",
     "endTime": "0500 PM",
     "instructorNames": "SHANKER, U",
     "meetingDay": " M W",
     "room": "0031",
     "startTime": "0400"
    },
    "sectionNumber": 210,
    "sectionType": "SECONDARY",
    "studentsEnrolled": 0,
    "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014/section/210",
    "waitlistSize": 0
   }
  ],
  "term": "B",
  "termYear": 2014,
  "uri": "https://apis-dev.berkeley.edu/cxf/asws/classoffering/STAT.2.Spring.2014"
 }
}"""

obj = json.loads(text)
for i in obj["ClassOffering"]["sections"]:
    print i["sectionNumber"]