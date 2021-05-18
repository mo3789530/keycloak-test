### Env 
Keycloak: 
Version 11.0.3
DB: PostgresSQl
Server PC:
OS Ubuntu 20.0.4
Core 4core8thread
Memory 16GB
Host on docker 
Client PC:
OS Windows 10
RESTAPI Client Postman


### CheckPoint 
Keycloak has a larger number of realms.
(About 500 realms created)
1. Token create performance.
token can get about 100ms.

2. Can I use admin console. 



This is sample decode token before add realms.
```json
{
  "exp": 1621146680,
  "iat": 1621146620,
  "jti": "9f8ec312-bb36-4420-bad5-bd385c9b8f2a",
  "iss": "http://localhost:8080/auth/realms/master",
  "aud": [
    "test-realm",
    "master-realm",
    "account"
  ],
  "sub": "44aacbb3-708f-481b-a5f7-a8704536fec2",
  "typ": "Bearer",
  "azp": "test",
  "session_state": "4e794cfa-20d5-4852-ad3c-0d35cdd2b869",
  "acr": "1",
  "realm_access": {
    "roles": [
      "create-realm",
      "offline_access",
      "admin",
      "uma_authorization"
    ]
  },
  "resource_access": {
    "master-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "account": {
      "roles": [
        "manage-account",
        "manage-account-links",
        "view-profile"
      ]
    }
  },
  "scope": "profile email",
  "email_verified": false,
  "preferred_username": "admin"
}

```

Token is very big after add 500 realms, because token include all realms roles.

```json
{
  "exp": 1621153517,
  "iat": 1621153457,
  "jti": "7a4f17f7-a979-4662-8e90-109ad14ca403",
  "iss": "http://localhost:8080/auth/realms/master",
  "aud": [
    "133-realm",
    "438-realm",
    "79-realm",
    "66-realm",
    "26-realm",
    "120-realm",
    "13-realm",
    "264-realm",
    "146-realm",
    "173-realm",
    "186-realm",
    "106-realm",
    "53-realm",
    "211-realm",
    "291-realm",
    "5-realm",
    "251-realm",
    "412-realm",
    "460-realm",
    "302-realm",
    "342-realm",
    "224-realm",
    "61-realm",
    "452-realm",
    "478-realm",
    "382-realm",
    "39-realm",
    "420-realm",
    "181-realm",
    "296-realm",
    "328-realm",
    "361-realm",
    "125-realm",
    "368-realm",
    "492-realm",
    "101-realm",
    "141-realm",
    "269-realm",
    "256-realm",
    "321-realm",
    "499-realm",
    "93-realm",
    "459-realm",
    "419-realm",
    "216-realm",
    "229-realm",
    "465-realm",
    "199-realm",
    "159-realm",
    "119-realm",
    "245-realm",
    "425-realm",
    "285-realm",
    "205-realm",
    "315-realm",
    "395-realm",
    "112-realm",
    "152-realm",
    "355-realm",
    "192-realm",
    "82-realm",
    "72-realm",
    "366-realm",
    "401-realm",
    "471-realm",
    "363-realm",
    "298-realm",
    "313-realm",
    "248-realm",
    "218-realm",
    "444-realm",
    "389-realm",
    "379-realm",
    "95-realm",
    "497-realm",
    "481-realm",
    "336-realm",
    "494-realm",
    "414-realm",
    "114-realm",
    "232-realm",
    "309-realm",
    "197-realm",
    "15-realm",
    "280-realm",
    "467-realm",
    "393-realm",
    "117-realm",
    "165-realm",
    "310-realm",
    "200-realm",
    "47-realm",
    "122-realm",
    "24-realm",
    "275-realm",
    "390-realm",
    "203-realm",
    "358-realm",
    "171-realm",
    "423-realm",
    "138-realm",
    "253-realm",
    "446-realm",
    "21-realm",
    "194-realm",
    "226-realm",
    "283-realm",
    "50-realm",
    "334-realm",
    "80-realm",
    "68-realm",
    "98-realm",
    "18-realm",
    "277-realm",
    "45-realm",
    "144-realm",
    "417-realm",
    "254-realm",
    "307-realm",
    "387-realm",
    "422-realm",
    "51-realm",
    "230-realm",
    "473-realm",
    "167-realm",
    "74-realm",
    "340-realm",
    "450-realm",
    "261-realm",
    "428-realm",
    "2-realm",
    "163-realm",
    "49-realm",
    "56-realm",
    "16-realm",
    "110-realm",
    "274-realm",
    "156-realm",
    "103-realm",
    "221-realm",
    "196-realm",
    "281-realm",
    "149-realm",
    "495-realm",
    "475-realm",
    "8-realm",
    "267-realm",
    "219-realm",
    "259-realm",
    "170-realm",
    "109-realm",
    "317-realm",
    "150-realm",
    "377-realm",
    "443-realm",
    "435-realm",
    "483-realm",
    "207-realm",
    "385-realm",
    "365-realm",
    "325-realm",
    "476-realm",
    "64-realm",
    "148-realm",
    "151-realm",
    "378-realm",
    "436-realm",
    "273-realm",
    "70-realm",
    "108-realm",
    "384-realm",
    "111-realm",
    "371-realm",
    "48-realm",
    "331-realm",
    "206-realm",
    "489-realm",
    "332-realm",
    "262-realm",
    "3-realm",
    "372-realm",
    "164-realm",
    "71-realm",
    "442-realm",
    "482-realm",
    "488-realm",
    "320-realm",
    "9-realm",
    "222-realm",
    "430-realm",
    "441-realm",
    "431-realm",
    "376-realm",
    "62-realm",
    "master-realm",
    "323-realm",
    "268-realm",
    "208-realm",
    "258-realm",
    "434-realm",
    "326-realm",
    "491-realm",
    "316-realm",
    "369-realm",
    "484-realm",
    "154-realm",
    "55-realm",
    "487-realm",
    "427-realm",
    "220-realm",
    "373-realm",
    "12-realm",
    "4-realm",
    "215-realm",
    "272-realm",
    "212-realm",
    "330-realm",
    "157-realm",
    "102-realm",
    "162-realm",
    "213-realm",
    "105-realm",
    "318-realm",
    "161-realm",
    "11-realm",
    "486-realm",
    "7-realm",
    "479-realm",
    "374-realm",
    "324-realm",
    "429-realm",
    "266-realm",
    "381-realm",
    "58-realm",
    "485-realm",
    "104-realm",
    "63-realm",
    "319-realm",
    "380-realm",
    "209-realm",
    "270-realm",
    "10-realm",
    "6-realm",
    "214-realm",
    "160-realm",
    "57-realm",
    "155-realm",
    "265-realm",
    "433-realm",
    "490-realm",
    "test2-realm",
    "375-realm",
    "418-realm",
    "271-realm",
    "153-realm",
    "99-realm",
    "113-realm",
    "59-realm",
    "46-realm",
    "100-realm",
    "86-realm",
    "126-realm",
    "284-realm",
    "193-realm",
    "231-realm",
    "166-realm",
    "33-realm",
    "73-realm",
    "322-realm",
    "204-realm",
    "20-realm",
    "314-realm",
    "362-realm",
    "81-realm",
    "244-realm",
    "432-realm",
    "472-realm",
    "41-realm",
    "498-realm",
    "388-realm",
    "19-realm",
    "458-realm",
    "400-realm",
    "440-realm",
    "480-realm",
    "466-realm",
    "158-realm",
    "54-realm",
    "223-realm",
    "413-realm",
    "263-realm",
    "426-realm",
    "198-realm",
    "354-realm",
    "118-realm",
    "60-realm",
    "394-realm",
    "78-realm",
    "38-realm",
    "290-realm",
    "25-realm",
    "187-realm",
    "437-realm",
    "257-realm",
    "297-realm",
    "250-realm",
    "65-realm",
    "327-realm",
    "477-realm",
    "180-realm",
    "140-realm",
    "367-realm",
    "210-realm",
    "383-realm",
    "107-realm",
    "453-realm",
    "493-realm",
    "217-realm",
    "14-realm",
    "147-realm",
    "94-realm",
    "451-realm",
    "356-realm",
    "421-realm",
    "386-realm",
    "343-realm",
    "52-realm",
    "333-realm",
    "278-realm",
    "228-realm",
    "306-realm",
    "474-realm",
    "359-realm",
    "329-realm",
    "424-realm",
    "1-realm",
    "252-realm",
    "447-realm",
    "370-realm",
    "260-realm",
    "75-realm",
    "174-realm",
    "255-realm",
    "145-realm",
    "67-realm",
    "137-realm",
    "142-realm",
    "168-realm",
    "341-realm",
    "44-realm",
    "115-realm",
    "308-realm",
    "496-realm",
    "416-realm",
    "469-realm",
    "364-realm",
    "299-realm",
    "121-realm",
    "311-realm",
    "439-realm",
    "391-realm",
    "276-realm",
    "139-realm",
    "249-realm",
    "312-realm",
    "195-realm",
    "22-realm",
    "392-realm",
    "225-realm",
    "17-realm",
    "282-realm",
    "97-realm",
    "445-realm",
    "468-realm",
    "202-realm",
    "172-realm",
    "335-realm",
    "123-realm",
    "408-realm",
    "143-realm",
    "89-realm",
    "69-realm",
    "36-realm",
    "294-realm",
    "76-realm",
    "201-realm",
    "136-realm",
    "183-realm",
    "176-realm",
    "23-realm",
    "43-realm",
    "116-realm",
    "241-realm",
    "357-realm",
    "287-realm",
    "247-realm",
    "239-realm",
    "397-realm",
    "189-realm",
    "96-realm",
    "129-realm",
    "190-realm",
    "169-realm",
    "337-realm",
    "415-realm",
    "463-realm",
    "130-realm",
    "227-realm",
    "455-realm",
    "84-realm",
    "305-realm",
    "345-realm",
    "338-realm",
    "233-realm",
    "188-realm",
    "403-realm",
    "191-realm",
    "135-realm",
    "31-realm",
    "344-realm",
    "279-realm",
    "30-realm",
    "88-realm",
    "449-realm",
    "286-realm",
    "409-realm",
    "246-realm",
    "83-realm",
    "124-realm",
    "360-realm",
    "304-realm",
    "234-realm",
    "402-realm",
    "37-realm",
    "42-realm",
    "77-realm",
    "175-realm",
    "448-realm",
    "470-realm",
    "303-realm",
    "92-realm",
    "461-realm",
    "396-realm",
    "411-realm",
    "288-realm",
    "353-realm",
    "238-realm",
    "85-realm",
    "test-realm",
    "404-realm",
    "346-realm",
    "349-realm",
    "339-realm",
    "454-realm",
    "464-realm",
    "399-realm",
    "35-realm",
    "177-realm",
    "407-realm",
    "134-realm",
    "32-realm",
    "235-realm",
    "185-realm",
    "292-realm",
    "240-realm",
    "27-realm",
    "87-realm",
    "295-realm",
    "350-realm",
    "182-realm",
    "351-realm",
    "178-realm",
    "456-realm",
    "348-realm",
    "128-realm",
    "243-realm",
    "293-realm",
    "406-realm",
    "40-realm",
    "131-realm",
    "289-realm",
    "90-realm",
    "236-realm",
    "301-realm",
    "28-realm",
    "242-realm",
    "457-realm",
    "352-realm",
    "179-realm",
    "237-realm",
    "347-realm",
    "91-realm",
    "462-realm",
    "300-realm",
    "184-realm",
    "405-realm",
    "127-realm",
    "29-realm",
    "398-realm",
    "34-realm",
    "410-realm",
    "132-realm",
    "account"
  ],
  "sub": "44aacbb3-708f-481b-a5f7-a8704536fec2",
  "typ": "Bearer",
  "azp": "test",
  "session_state": "37588b4d-47bd-4508-bceb-21a8bbc43aa7",
  "acr": "1",
  "realm_access": {
    "roles": [
      "create-realm",
      "offline_access",
      "admin",
      "uma_authorization"
    ]
  },
  "resource_access": {
    "133-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "438-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "79-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "66-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "26-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "120-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "13-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "264-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "146-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "173-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "186-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "106-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "53-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "211-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "291-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "5-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "251-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "412-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "460-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "302-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "342-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "224-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "61-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "452-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "478-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "382-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "39-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "420-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "181-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "296-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "328-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "361-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "125-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "368-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "492-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "101-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "141-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "269-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "256-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "321-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "499-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "93-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "459-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "419-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "216-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "229-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "465-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "199-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "159-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "119-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "245-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "425-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "285-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "205-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "315-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "395-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "112-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "152-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "355-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "192-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "82-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "72-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "366-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "401-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "471-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "363-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "298-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "313-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "248-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "218-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "444-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "389-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "379-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "95-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "497-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "481-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "336-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "494-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "414-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "114-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "232-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "309-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "197-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "15-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "280-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "467-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "393-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "117-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "165-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "310-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "200-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "47-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "122-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "24-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "275-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "390-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "203-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "358-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "171-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "423-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "138-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "253-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "446-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "21-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "194-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "226-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "283-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "50-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "334-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "80-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "68-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "98-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "18-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "277-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "45-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "144-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "417-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "254-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "307-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "387-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "422-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "51-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "230-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "473-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "167-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "74-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "340-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "450-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "261-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "428-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "2-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "163-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "49-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "56-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "16-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "110-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "274-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "156-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "103-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "221-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "196-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "281-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "149-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "495-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "475-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "8-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "267-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "219-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "259-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "170-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "109-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "317-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "150-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "377-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "443-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "435-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "483-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "207-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "385-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "365-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "325-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "476-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "64-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "148-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "151-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "378-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "436-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "273-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "70-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "108-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "384-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "111-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "371-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "48-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "331-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "206-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "489-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "332-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "262-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "3-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "372-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "164-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "71-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "442-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "482-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "488-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "320-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "9-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "222-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "430-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "441-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "431-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "376-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "62-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "master-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "323-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "268-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "208-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "258-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "434-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "326-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "491-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "316-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "369-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "484-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "154-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "55-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "487-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "427-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "220-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "373-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "12-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "4-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "215-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "272-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "212-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "330-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "157-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "102-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "162-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "213-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "105-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "318-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "161-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "11-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "486-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "7-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "479-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "374-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "324-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "429-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "266-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "381-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "58-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "485-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "104-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "63-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "319-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "380-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "209-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "270-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "10-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "6-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "214-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "160-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "57-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "155-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "265-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "433-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "490-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "test2-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "375-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "418-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "271-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "153-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "99-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "113-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "59-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "46-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "100-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "86-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "126-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "284-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "193-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "231-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "166-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "33-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "73-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "322-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "204-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "20-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "314-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "362-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "81-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "244-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "432-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "472-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "41-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "498-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "388-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "19-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "458-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "400-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "440-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "480-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "466-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "158-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "54-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "223-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "413-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "263-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "426-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "198-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "354-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "118-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "60-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "394-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "78-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "38-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "290-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "25-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "187-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "437-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "257-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "297-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "250-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "65-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "327-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "477-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "180-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "140-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "367-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "210-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "383-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "107-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "453-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "493-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "217-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "14-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "147-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "94-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "451-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "356-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "421-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "386-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "343-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "52-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "333-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "278-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "228-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "306-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "474-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "359-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "329-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "424-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "1-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "252-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "447-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "370-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "260-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "75-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "174-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "255-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "145-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "67-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "137-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "142-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "168-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "341-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "44-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "115-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "308-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "496-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "416-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "469-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "364-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "299-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "121-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "311-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "439-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "391-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "276-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "139-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "249-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "312-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "195-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "22-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "392-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "225-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "17-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "282-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "97-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "445-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "468-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "202-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "172-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "335-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "123-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "408-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "143-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "89-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "69-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "36-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "294-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "76-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "201-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "136-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "183-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "176-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "23-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "43-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "116-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "241-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "357-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "287-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "247-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "239-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "397-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "189-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "96-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "129-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "190-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "169-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "337-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "415-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "463-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "130-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "227-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "455-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "84-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "305-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "345-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "338-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "233-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "188-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "403-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "191-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "135-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "31-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "344-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "279-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "30-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "88-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "449-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "286-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "409-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "246-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "83-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "124-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "360-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "304-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "234-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "402-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "37-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "42-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "77-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "175-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "448-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "470-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "303-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "92-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "461-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "396-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "411-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "288-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "353-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "238-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "85-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "test-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "404-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "346-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "349-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "339-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "454-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "464-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "399-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "35-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "177-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "407-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "134-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "32-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "235-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "185-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "292-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "240-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "27-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "87-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "295-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "350-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "182-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "351-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "178-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "456-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "348-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "128-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "243-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "293-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "406-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "40-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "131-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "289-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "90-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "236-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "301-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "28-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "242-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "457-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "352-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "179-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "237-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "347-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "91-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "462-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "300-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "184-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "405-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "127-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "29-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "398-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "34-realm": {
      "roles": [
        "view-identity-providers",
        "view-realm",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "410-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "132-realm": {
      "roles": [
        "view-realm",
        "view-identity-providers",
        "manage-identity-providers",
        "impersonation",
        "create-client",
        "manage-users",
        "query-realms",
        "view-authorization",
        "query-clients",
        "query-users",
        "manage-events",
        "manage-realm",
        "view-events",
        "view-users",
        "view-clients",
        "manage-authorization",
        "manage-clients",
        "query-groups"
      ]
    },
    "account": {
      "roles": [
        "manage-account",
        "manage-account-links",
        "view-profile"
      ]
    }
  },
  "scope": "profile email",
  "email_verified": false,
  "preferred_username": "admin"
}
```


Response time is not slowey 
```
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
139 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
158 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
213 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
190 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
126 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
121 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
212 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
146 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
152 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
138 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
627 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
632 ms
 
POST http://t440p:8080/auth/realms/master/protocol/openid-connect/token
200
121 ms

```


https://stackoverflow.com/questions/56743109/keycloak-create-admin-user-in-a-realm  
Create regular user in a realm:  
Open admin console and select realm of your choice (realm selection box on top left side).  
Go to users (sidebar) -> add user (button on the right side)  
Fill in required fields and press save button.  
Open Credentials tab and set password.  
Open Role Mapping tab:  
Select realm-management under Client Roles.  
Select all available roles and press Add selected.  
Go to http://keycloak/auth/admin/REALM_NAME/console (replace REALM_NAME with realm name in which you created the user) and login.  
You should see admin UI only for this realm.  




```
Last login: Fri Jan  1 09:37:58 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
monoMacBook-Pro:~ mo3789530$ ssh mo@192.168.11.9
mo@192.168.11.9's password: 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-53-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage



Your Hardware Enablement Stack (HWE) is supported until April 2025.
Last login: Mon May 17 13:20:33 2021 from 192.168.11.7
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/py/
keyclaok-test/ nmp/           policy-data/   python-tools/  sample/        
mo@macmini:~$ cd repo/py/
keyclaok-test/ nmp/           policy-data/   python-tools/  sample/        
mo@macmini:~$ cd repo/py/
keyclaok-test/ nmp/           policy-data/   python-tools/  sample/        
mo@macmini:~$ cd repo/py/keyclaok-test/
mo@macmini:~/repo/py/keyclaok-test$ ls
data  doc  docker  src
mo@macmini:~/repo/py/keyclaok-test$ docker ps 
CONTAINER ID   IMAGE                              COMMAND                  CREATED        STATUS        PORTS                              NAMES
8c9a80b5fb1f   quay.io/keycloak/keycloak:11.0.3   "/opt/jboss/tools/do…"   19 hours ago   Up 19 hours   0.0.0.0:8080->8080/tcp, 8443/tcp   docker_keycloak_1
c931c3c67377   postgres                           "docker-entrypoint.s…"   19 hours ago   Up 19 hours   5432/tcp                           docker_postgres_1
mo@macmini:~/repo/py/keyclaok-test$ cd doc
mo@macmini:~/repo/py/keyclaok-test/doc$ cd ..
mo@macmini:~/repo/py/keyclaok-test$ cd doc
doc/    docker/ 
mo@macmini:~/repo/py/keyclaok-test$ cd doc
doc/    docker/ 
mo@macmini:~/repo/py/keyclaok-test$ cd docker/
mo@macmini:~/repo/py/keyclaok-test/docker$ docker-compose down
Stopping docker_keycloak_1 ... done
Stopping docker_postgres_1 ... done
Removing docker_keycloak_1 ... done
Removing docker_postgres_1 ... done
Removing network docker_default
mo@macmini:~/repo/py/keyclaok-test/docker$ docker vloume
docker: 'vloume' is not a docker command.
See 'docker --help'
mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume

Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes

Run 'docker volume COMMAND --help' for more information on a command.
mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume ls
DRIVER    VOLUME NAME
local     2d0a6da88aee46ec90bb1fae72efd971301c958cf9f07e3b9060a2c85689bde6
local     22d9c2a46418182268b9a0090f98868f572a8014463aabe6d09f63d145f2118a
local     630d48d8128386b39e279535ce327c6e22f5ee8dd6176f416c432ae3f4222014
local     5960e4e0c1903cbb84349b58c9bd950a9d5980b7447eaf88e3a3e6d38bbab200
local     6875723f3a7d349ea5d6456014339ad3a955929c25caa2ccc99469aad72d87c7
local     dac286882930459ec1decf3506a7e27f377d3a09ec22edd186e6207c47e61129
local     docker_postgres_data
local     src_postgres_data
mo@macmini:~/repo/py/keyclaok-test/docker$ dokcer volume rm src_postgres_data

Command 'dokcer' not found, did you mean:

  command 'docker' from snap docker (19.03.13)
  command 'docker' from deb docker.io (20.10.2-0ubuntu1~20.04.2)

See 'snap info <snapname>' for additional versions.

mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume rm src_postgres_data
src_postgres_data
mo@macmini:~/repo/py/keyclaok-test/docker$ docker-compose up -d
Creating network "docker_default" with the default driver
Creating docker_postgres_1 ... done
Creating docker_keycloak_1 ... done
mo@macmini:~/repo/py/keyclaok-test/docker$ cat docker-compose.yaml 
version: '3'

volumes:
  postgres_data:
      driver: local

services:
  postgres:
      image: postgres
      volumes:
        - postgres_data:/var/lib/postgresql/data
      environment:
        POSTGRES_DB: keycloak
        POSTGRES_USER: keycloak
        POSTGRES_PASSWORD: password
  keycloak:
      image: quay.io/keycloak/keycloak:11.0.3
      environment:
        DB_VENDOR: POSTGRES
        DB_ADDR: postgres
        DB_DATABASE: keycloak
        DB_USER: keycloak
        DB_SCHEMA: public
        DB_PASSWORD: password
        KEYCLOAK_USER: admin
        KEYCLOAK_PASSWORD: Pa55w0rd
        JAVA_OPTS: "-Xmx1024m -Xms1024m"
        # Uncomment the line below if you want to specify JDBC parameters. The parameter below is just an example, and it shouldn't be used in production without knowledge. It is highly recommended that you read the PostgreSQL JDBC driver documentation in order to use it.
        #JDBC_PARAMS: "ssl=true"
      ports:
        - 8080:8080
      depends_on:
        - postgres
      # deploy:
      #   resources:
      #     limits:
      #       cpus: "1"mo@macmini:~/repo/py/keyclaok-test/docker$ docker-compose down
Stopping docker_keycloak_1 ... done
Stopping docker_postgres_1 ... done
Removing docker_keycloak_1 ... done
Removing docker_postgres_1 ... done
Removing network docker_default
mo@macmini:~/repo/py/keyclaok-test/docker$ dokcer volume rm src_postgres_data

Command 'dokcer' not found, did you mean:

  command 'docker' from snap docker (19.03.13)
  command 'docker' from deb docker.io (20.10.2-0ubuntu1~20.04.2)

See 'snap info <snapname>' for additional versions.

mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume rm src_postgres_data
Error: No such volume: src_postgres_data
mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume ls
DRIVER    VOLUME NAME
local     2d0a6da88aee46ec90bb1fae72efd971301c958cf9f07e3b9060a2c85689bde6
local     22d9c2a46418182268b9a0090f98868f572a8014463aabe6d09f63d145f2118a
local     630d48d8128386b39e279535ce327c6e22f5ee8dd6176f416c432ae3f4222014
local     5960e4e0c1903cbb84349b58c9bd950a9d5980b7447eaf88e3a3e6d38bbab200
local     6875723f3a7d349ea5d6456014339ad3a955929c25caa2ccc99469aad72d87c7
local     dac286882930459ec1decf3506a7e27f377d3a09ec22edd186e6207c47e61129
local     docker_postgres_data
mo@macmini:~/repo/py/keyclaok-test/docker$ docker volume rm docker_postgres_data
docker_postgres_data
mo@macmini:~/repo/py/keyclaok-test/docker$ docker-compose up -d
Creating network "docker_default" with the default driver
Creating volume "docker_postgres_data" with local driver
Creating docker_postgres_1 ... done
Creating docker_keycloak_1 ... done
mo@macmini:~/repo/py/keyclaok-test/docker$ 
mo@macmini:~/repo/py/keyclaok-test/docker$ 
mo@macmini:~/repo/py/keyclaok-test/docker$ 
mo@macmini:~/repo/py/keyclaok-test/docker$ cd ..
mo@macmini:~/repo/py/keyclaok-test$ ls
data  doc  docker  src
mo@macmini:~/repo/py/keyclaok-test$ cd src/
mo@macmini:~/repo/py/keyclaok-test/src$ ls
keycloak2.py  keycloak.py
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak2
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak2.py 
mo@macmini:~/repo/py/keyclaok-test/src$ python3 keycloak2.py 
start
token: 0.143223
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [201]>
token: 0.140212
{'id': '139', 'realm': '139', 'enabled': True}
<Response [201]>
realm: 1.310277
token: 0.176715
{'id': '140', 'realm': '140', 'enabled': True}
<Response [201]>
realm: 0.899756
token: 0.17672
{'id': '141', 'realm': '141', 'enabled': True}
<Response [201]>
realm: 1.106897
token: 0.176943
{'id': '142', 'realm': '142', 'enabled': True}
<Response [201]>
realm: 0.81585
token: 0.181037
{'id': '143', 'realm': '143', 'enabled': True}
<Response [201]>
realm: 0.761636
token: 0.162982
{'id': '144', 'realm': '144', 'enabled': True}
<Response [201]>
realm: 0.753673
token: 0.173253
{'id': '145', 'realm': '145', 'enabled': True}
<Response [201]>
realm: 0.771796
token: 0.160037
{'id': '146', 'realm': '146', 'enabled': True}
<Response [201]>
realm: 0.700411
token: 0.165406
{'id': '147', 'realm': '147', 'enabled': True}
<Response [201]>
realm: 0.780239
token: 0.168388
{'id': '148', 'realm': '148', 'enabled': True}
<Response [201]>
realm: 0.795491
token: 0.165855
{'id': '149', 'realm': '149', 'enabled': True}
<Response [201]>
realm: 0.738551
token: 0.162401
{'id': '150', 'realm': '150', 'enabled': True}
<Response [201]>
realm: 0.724755
token: 0.166054
{'id': '151', 'realm': '151', 'enabled': True}
<Response [201]>
realm: 0.919797
token: 0.161393
{'id': '152', 'realm': '152', 'enabled': True}
<Response [201]>
realm: 0.816032
token: 0.180086
{'id': '153', 'realm': '153', 'enabled': True}
<Response [201]>
realm: 0.778638
token: 0.168791
{'id': '154', 'realm': '154', 'enabled': True}
<Response [201]>
realm: 0.869828
token: 0.161094
{'id': '155', 'realm': '155', 'enabled': True}
<Response [201]>
realm: 0.762034
token: 0.171201
{'id': '156', 'realm': '156', 'enabled': True}
<Response [201]>
realm: 1.132494
token: 0.174022
{'id': '157', 'realm': '157', 'enabled': True}
<Response [201]>
realm: 0.847977
token: 0.174524
{'id': '158', 'realm': '158', 'enabled': True}
<Response [201]>
realm: 0.822051
token: 0.168828
{'id': '159', 'realm': '159', 'enabled': True}
<Response [201]>
realm: 0.877998
token: 0.171689
{'id': '160', 'realm': '160', 'enabled': True}
<Response [201]>
realm: 0.798269
token: 0.165791
{'id': '161', 'realm': '161', 'enabled': True}
<Response [201]>
realm: 0.80191
token: 0.176641
{'id': '162', 'realm': '162', 'enabled': True}
<Response [201]>
realm: 0.774087
token: 0.162159
{'id': '163', 'realm': '163', 'enabled': True}
<Response [201]>
realm: 0.850459
token: 0.165962
{'id': '164', 'realm': '164', 'enabled': True}
<Response [201]>
realm: 0.887871
token: 0.170064
{'id': '165', 'realm': '165', 'enabled': True}
<Response [201]>
realm: 0.930294
token: 0.165872
{'id': '166', 'realm': '166', 'enabled': True}
<Response [201]>
realm: 0.862076
token: 0.167741
{'id': '167', 'realm': '167', 'enabled': True}
<Response [201]>
realm: 0.936005
token: 0.170846
{'id': '168', 'realm': '168', 'enabled': True}
<Response [201]>
realm: 0.943794
token: 0.169409
{'id': '169', 'realm': '169', 'enabled': True}
<Response [201]>
realm: 0.999004
token: 0.166206
{'id': '170', 'realm': '170', 'enabled': True}
<Response [201]>
realm: 1.049809
token: 0.174475
{'id': '171', 'realm': '171', 'enabled': True}
<Response [201]>
realm: 1.111311
token: 0.165018
{'id': '172', 'realm': '172', 'enabled': True}
<Response [201]>
realm: 0.897276
token: 0.176001
{'id': '173', 'realm': '173', 'enabled': True}
<Response [201]>
realm: 1.029997
token: 0.16882
{'id': '174', 'realm': '174', 'enabled': True}
<Response [201]>
realm: 1.009104
token: 0.168811
{'id': '175', 'realm': '175', 'enabled': True}
<Response [201]>
realm: 1.086873
token: 0.168405
{'id': '176', 'realm': '176', 'enabled': True}
<Response [201]>
realm: 1.081659
token: 0.181683
{'id': '177', 'realm': '177', 'enabled': True}
<Response [201]>
realm: 1.093818
token: 0.173045
{'id': '178', 'realm': '178', 'enabled': True}
<Response [201]>
realm: 1.093942
token: 0.174186
{'id': '179', 'realm': '179', 'enabled': True}
<Response [201]>
realm: 1.229579
token: 0.174102
{'id': '180', 'realm': '180', 'enabled': True}
<Response [201]>
realm: 1.135433
token: 0.182241
{'id': '181', 'realm': '181', 'enabled': True}
<Response [201]>
realm: 1.624365
token: 0.176591
{'id': '182', 'realm': '182', 'enabled': True}
<Response [201]>
realm: 1.115875
token: 0.173819
{'id': '183', 'realm': '183', 'enabled': True}
<Response [201]>
realm: 1.315694
token: 0.170287
{'id': '184', 'realm': '184', 'enabled': True}
<Response [201]>
realm: 1.122803
token: 0.176995
{'id': '185', 'realm': '185', 'enabled': True}
<Response [201]>
realm: 1.281109
token: 0.172513
{'id': '186', 'realm': '186', 'enabled': True}
<Response [201]>
realm: 1.128313
token: 0.176088
{'id': '187', 'realm': '187', 'enabled': True}
<Response [201]>
realm: 1.155782
token: 0.175471
{'id': '188', 'realm': '188', 'enabled': True}
<Response [201]>
realm: 1.429139
token: 0.173105
{'id': '189', 'realm': '189', 'enabled': True}
<Response [201]>
realm: 1.276209
token: 0.178349
{'id': '190', 'realm': '190', 'enabled': True}
<Response [201]>
realm: 1.431272
token: 0.183731
{'id': '191', 'realm': '191', 'enabled': True}
<Response [201]>
realm: 1.420076
token: 0.177276
{'id': '192', 'realm': '192', 'enabled': True}
<Response [201]>
realm: 1.330912
token: 0.177065
{'id': '193', 'realm': '193', 'enabled': True}
<Response [201]>
realm: 1.317018
token: 0.173542
{'id': '194', 'realm': '194', 'enabled': True}
<Response [201]>
realm: 1.332619
token: 0.178117
{'id': '195', 'realm': '195', 'enabled': True}
<Response [201]>
realm: 1.366481
token: 0.181142
{'id': '196', 'realm': '196', 'enabled': True}
<Response [201]>
realm: 1.301575
token: 0.199924
{'id': '197', 'realm': '197', 'enabled': True}
<Response [201]>
realm: 1.36433
token: 0.182103
{'id': '198', 'realm': '198', 'enabled': True}
<Response [201]>
realm: 1.319494
token: 0.18443
{'id': '199', 'realm': '199', 'enabled': True}
<Response [201]>
realm: 1.732721
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak2.py 
mo@macmini:~/repo/py/keyclaok-test/src$ python3 keycloak2.py 
start
token: 0.187089
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [409]>
token: 0.137227
{'id': '1', 'realm': '1', 'enabled': True}
<Response [201]>
realm: 1.389024
token: 0.19196
{'id': '2', 'realm': '2', 'enabled': True}
<Response [201]>
realm: 1.410991
token: 0.191734
{'id': '3', 'realm': '3', 'enabled': True}
<Response [201]>
realm: 1.450987
token: 0.2256
{'id': '4', 'realm': '4', 'enabled': True}
<Response [201]>
realm: 1.5334
token: 0.187911
{'id': '5', 'realm': '5', 'enabled': True}
<Response [201]>
realm: 1.438113
token: 0.182493
{'id': '6', 'realm': '6', 'enabled': True}
<Response [201]>
realm: 1.438596
token: 0.185403
{'id': '7', 'realm': '7', 'enabled': True}
<Response [201]>
realm: 1.444742
token: 0.19384
{'id': '8', 'realm': '8', 'enabled': True}
<Response [201]>
realm: 1.538712
token: 0.184879
{'id': '9', 'realm': '9', 'enabled': True}
<Response [201]>
realm: 1.719993
token: 0.184329
{'id': '10', 'realm': '10', 'enabled': True}
<Response [201]>
realm: 1.505265
token: 0.191027
{'id': '11', 'realm': '11', 'enabled': True}
<Response [201]>
realm: 1.704745
token: 0.195688
{'id': '12', 'realm': '12', 'enabled': True}
<Response [201]>
realm: 1.868403
token: 0.181016
{'id': '13', 'realm': '13', 'enabled': True}
<Response [201]>
realm: 1.568504
token: 0.184536
{'id': '14', 'realm': '14', 'enabled': True}
<Response [201]>
realm: 1.652625
token: 0.179843
{'id': '15', 'realm': '15', 'enabled': True}
<Response [201]>
realm: 1.535004
token: 0.189957
{'id': '16', 'realm': '16', 'enabled': True}
<Response [201]>
realm: 1.64328
token: 0.182884
{'id': '17', 'realm': '17', 'enabled': True}
<Response [201]>
realm: 1.612717
token: 0.189787
{'id': '18', 'realm': '18', 'enabled': True}
<Response [201]>
realm: 1.677219
token: 0.186791
{'id': '19', 'realm': '19', 'enabled': True}
<Response [201]>
realm: 1.748656
token: 0.191952
{'id': '20', 'realm': '20', 'enabled': True}
<Response [201]>
realm: 1.886947
token: 0.203996
{'id': '21', 'realm': '21', 'enabled': True}
<Response [201]>
realm: 1.704377
token: 0.183872
{'id': '22', 'realm': '22', 'enabled': True}
<Response [201]>
realm: 1.838944
token: 0.201942
{'id': '23', 'realm': '23', 'enabled': True}
<Response [201]>
realm: 1.894977
token: 0.187657
{'id': '24', 'realm': '24', 'enabled': True}
<Response [201]>
realm: 1.715081
token: 0.195131
{'id': '25', 'realm': '25', 'enabled': True}
<Response [201]>
realm: 1.784388
token: 0.192974
{'id': '26', 'realm': '26', 'enabled': True}
<Response [201]>
realm: 1.748871
token: 0.203326
{'id': '27', 'realm': '27', 'enabled': True}
<Response [201]>
realm: 1.925241
token: 0.216031
{'id': '28', 'realm': '28', 'enabled': True}
<Response [201]>
realm: 1.767115
token: 0.195829
{'id': '29', 'realm': '29', 'enabled': True}
<Response [201]>
realm: 1.773553
token: 0.190377
{'id': '30', 'realm': '30', 'enabled': True}
<Response [201]>
realm: 1.857645
token: 0.201212
{'id': '31', 'realm': '31', 'enabled': True}
<Response [201]>
realm: 1.792274
token: 0.190623
{'id': '32', 'realm': '32', 'enabled': True}
<Response [201]>
realm: 1.809806
token: 0.191195
{'id': '33', 'realm': '33', 'enabled': True}
<Response [201]>
realm: 1.892158
token: 0.198758
{'id': '34', 'realm': '34', 'enabled': True}
<Response [201]>
realm: 1.847632
token: 0.196076
{'id': '35', 'realm': '35', 'enabled': True}
<Response [201]>
realm: 2.024426
token: 0.19587
{'id': '36', 'realm': '36', 'enabled': True}
<Response [201]>
realm: 1.902455
token: 0.197237
{'id': '37', 'realm': '37', 'enabled': True}
<Response [201]>
realm: 1.931828
token: 0.201576
{'id': '38', 'realm': '38', 'enabled': True}
<Response [201]>
realm: 2.109117
token: 0.19673
{'id': '39', 'realm': '39', 'enabled': True}
<Response [201]>
realm: 1.972421
token: 0.198028
{'id': '40', 'realm': '40', 'enabled': True}
<Response [201]>
realm: 1.969425
token: 0.193307
{'id': '41', 'realm': '41', 'enabled': True}
<Response [201]>
realm: 2.068211
token: 0.206992
{'id': '42', 'realm': '42', 'enabled': True}
<Response [201]>
realm: 2.220301
token: 0.20007
{'id': '43', 'realm': '43', 'enabled': True}
<Response [201]>
realm: 2.051532
token: 0.200052
{'id': '44', 'realm': '44', 'enabled': True}
<Response [201]>
realm: 1.999286
token: 0.200278
{'id': '45', 'realm': '45', 'enabled': True}
<Response [201]>
realm: 1.996001
token: 0.193509
{'id': '46', 'realm': '46', 'enabled': True}
<Response [201]>
realm: 2.083057
token: 0.200846
{'id': '47', 'realm': '47', 'enabled': True}
<Response [201]>
realm: 2.026986
token: 0.199517
{'id': '48', 'realm': '48', 'enabled': True}
<Response [201]>
realm: 2.102
token: 0.193995
{'id': '49', 'realm': '49', 'enabled': True}
<Response [201]>
realm: 2.096083
token: 0.200214
{'id': '50', 'realm': '50', 'enabled': True}
<Response [201]>
realm: 2.150422
token: 0.205376
{'id': '51', 'realm': '51', 'enabled': True}
<Response [201]>
realm: 2.144025
token: 0.206608
{'id': '52', 'realm': '52', 'enabled': True}
<Response [201]>
realm: 2.24362
token: 0.206805
{'id': '53', 'realm': '53', 'enabled': True}
<Response [201]>
realm: 2.29117
token: 0.197579
{'id': '54', 'realm': '54', 'enabled': True}
<Response [201]>
realm: 2.220521
token: 0.208975
{'id': '55', 'realm': '55', 'enabled': True}
<Response [201]>
realm: 2.201988
token: 0.218464
{'id': '56', 'realm': '56', 'enabled': True}
<Response [201]>
realm: 2.22942
token: 0.208865
{'id': '57', 'realm': '57', 'enabled': True}
<Response [201]>
realm: 2.323372
token: 0.206364
{'id': '58', 'realm': '58', 'enabled': True}
<Response [201]>
realm: 2.379837
token: 0.205975
{'id': '59', 'realm': '59', 'enabled': True}
<Response [201]>
realm: 2.312627
token: 0.20595
{'id': '60', 'realm': '60', 'enabled': True}
<Response [201]>
realm: 2.426482
token: 0.22091
{'id': '61', 'realm': '61', 'enabled': True}
<Response [201]>
realm: 2.332832
token: 0.207999
{'id': '62', 'realm': '62', 'enabled': True}
<Response [201]>
realm: 2.34089
token: 0.210643
{'id': '63', 'realm': '63', 'enabled': True}
<Response [201]>
realm: 2.37012
token: 0.206414
{'id': '64', 'realm': '64', 'enabled': True}
<Response [201]>
realm: 2.331161
token: 0.208701
{'id': '65', 'realm': '65', 'enabled': True}
<Response [201]>
realm: 2.353237
token: 0.199624
{'id': '66', 'realm': '66', 'enabled': True}
<Response [201]>
realm: 2.393046
token: 0.205983
{'id': '67', 'realm': '67', 'enabled': True}
<Response [201]>
realm: 2.485929
token: 0.206119
{'id': '68', 'realm': '68', 'enabled': True}
<Response [201]>
realm: 2.519347
token: 0.219753
{'id': '69', 'realm': '69', 'enabled': True}
<Response [201]>
realm: 2.489821
token: 0.212954
{'id': '70', 'realm': '70', 'enabled': True}
<Response [201]>
realm: 2.684934
token: 0.205039
{'id': '71', 'realm': '71', 'enabled': True}
<Response [201]>
realm: 2.511319
token: 0.214064
{'id': '72', 'realm': '72', 'enabled': True}
<Response [201]>
realm: 2.34909
token: 0.211278
{'id': '73', 'realm': '73', 'enabled': True}
<Response [201]>
realm: 2.627467
token: 0.209042
{'id': '74', 'realm': '74', 'enabled': True}
<Response [201]>
realm: 2.610023
token: 0.230268
{'id': '75', 'realm': '75', 'enabled': True}
<Response [201]>
realm: 2.668582
token: 0.211967
{'id': '76', 'realm': '76', 'enabled': True}
<Response [201]>
realm: 2.548193
token: 0.209429
{'id': '77', 'realm': '77', 'enabled': True}
<Response [201]>
realm: 2.549401
token: 0.212329
{'id': '78', 'realm': '78', 'enabled': True}
<Response [201]>
realm: 2.578654
token: 0.212105
{'id': '79', 'realm': '79', 'enabled': True}
<Response [201]>
realm: 2.630003
token: 0.210193
{'id': '80', 'realm': '80', 'enabled': True}
<Response [201]>
realm: 2.722893
token: 0.219454
{'id': '81', 'realm': '81', 'enabled': True}
<Response [201]>
realm: 2.785239
token: 0.246162
{'id': '82', 'realm': '82', 'enabled': True}
<Response [201]>
realm: 2.855393
token: 0.221082
{'id': '83', 'realm': '83', 'enabled': True}
<Response [201]>
realm: 2.708581
token: 0.211743
{'id': '84', 'realm': '84', 'enabled': True}
<Response [201]>
realm: 2.934026
token: 0.218724
{'id': '85', 'realm': '85', 'enabled': True}
<Response [201]>
realm: 2.721896
token: 0.217999
{'id': '86', 'realm': '86', 'enabled': True}
<Response [201]>
realm: 2.703675
token: 0.214528
{'id': '87', 'realm': '87', 'enabled': True}
<Response [201]>
realm: 2.742145
token: 0.218589
{'id': '88', 'realm': '88', 'enabled': True}
<Response [201]>
realm: 2.78492
token: 0.218745
{'id': '89', 'realm': '89', 'enabled': True}
<Response [201]>
realm: 2.88545
token: 0.226702
{'id': '90', 'realm': '90', 'enabled': True}
<Response [201]>
realm: 2.967544
token: 0.219085
{'id': '91', 'realm': '91', 'enabled': True}
<Response [201]>
realm: 2.869687
token: 0.2198
{'id': '92', 'realm': '92', 'enabled': True}
<Response [201]>
realm: 2.875815
token: 0.221997
{'id': '93', 'realm': '93', 'enabled': True}
<Response [201]>
realm: 2.911095
token: 0.219011
{'id': '94', 'realm': '94', 'enabled': True}
<Response [201]>
realm: 2.877587
token: 0.211782
{'id': '95', 'realm': '95', 'enabled': True}
<Response [201]>
realm: 2.838012
token: 0.225654
{'id': '96', 'realm': '96', 'enabled': True}
<Response [201]>
realm: 2.94075
token: 0.224405
{'id': '97', 'realm': '97', 'enabled': True}
<Response [201]>
realm: 2.765968
token: 0.22156
{'id': '98', 'realm': '98', 'enabled': True}
<Response [201]>
realm: 2.946151
token: 0.225103
{'id': '99', 'realm': '99', 'enabled': True}
<Response [201]>
realm: 2.918709
token: 0.219139
{'id': '100', 'realm': '100', 'enabled': True}
<Response [201]>
realm: 2.907357
token: 0.220784
{'id': '101', 'realm': '101', 'enabled': True}
<Response [201]>
realm: 2.962513
token: 0.227265
{'id': '102', 'realm': '102', 'enabled': True}
<Response [201]>
realm: 2.933204
token: 0.224808
{'id': '103', 'realm': '103', 'enabled': True}
<Response [201]>
realm: 2.943199
token: 0.226266
{'id': '104', 'realm': '104', 'enabled': True}
<Response [201]>
realm: 3.036183
token: 0.228735
{'id': '105', 'realm': '105', 'enabled': True}
<Response [201]>
realm: 3.022455
token: 0.221984
{'id': '106', 'realm': '106', 'enabled': True}
<Response [201]>
realm: 3.030812
token: 0.224766
{'id': '107', 'realm': '107', 'enabled': True}
<Response [201]>
realm: 3.069663
token: 0.224234
{'id': '108', 'realm': '108', 'enabled': True}
<Response [201]>
realm: 3.044803
token: 0.231219
{'id': '109', 'realm': '109', 'enabled': True}
<Response [201]>
realm: 3.095704
token: 0.255341
{'id': '110', 'realm': '110', 'enabled': True}
<Response [201]>
realm: 3.13161
token: 0.236294
{'id': '111', 'realm': '111', 'enabled': True}
<Response [201]>
realm: 3.142774
token: 0.231382
{'id': '112', 'realm': '112', 'enabled': True}
<Response [201]>
realm: 3.46772
token: 0.252401
{'id': '113', 'realm': '113', 'enabled': True}
<Response [201]>
realm: 3.176741
token: 0.229154
{'id': '114', 'realm': '114', 'enabled': True}
<Response [201]>
realm: 3.170321
token: 0.23401
{'id': '115', 'realm': '115', 'enabled': True}
<Response [201]>
realm: 3.2795
token: 0.227879
{'id': '116', 'realm': '116', 'enabled': True}
<Response [201]>
realm: 3.291878
token: 0.239314
{'id': '117', 'realm': '117', 'enabled': True}
<Response [201]>
realm: 3.222275
token: 0.218685
{'id': '118', 'realm': '118', 'enabled': True}
<Response [201]>
realm: 3.253742
token: 0.237774
{'id': '119', 'realm': '119', 'enabled': True}
<Response [201]>
realm: 3.225185
token: 0.22994
{'id': '120', 'realm': '120', 'enabled': True}
<Response [201]>
realm: 3.843447
token: 0.238234
{'id': '121', 'realm': '121', 'enabled': True}
<Response [201]>
realm: 3.320027
token: 0.239416
{'id': '122', 'realm': '122', 'enabled': True}
<Response [201]>
realm: 3.305894
token: 0.236917
{'id': '123', 'realm': '123', 'enabled': True}
<Response [201]>
realm: 3.331055
token: 0.231619
{'id': '124', 'realm': '124', 'enabled': True}
<Response [201]>
realm: 3.542572
token: 0.238236
{'id': '125', 'realm': '125', 'enabled': True}
<Response [201]>
realm: 3.434729
token: 0.247993
{'id': '126', 'realm': '126', 'enabled': True}
<Response [201]>
realm: 3.461458
token: 0.241502
{'id': '127', 'realm': '127', 'enabled': True}
<Response [201]>
realm: 3.434196
token: 0.234892
{'id': '128', 'realm': '128', 'enabled': True}
<Response [201]>
realm: 3.474593
token: 0.245207
{'id': '129', 'realm': '129', 'enabled': True}
<Response [201]>
realm: 3.437534
token: 0.24008
{'id': '130', 'realm': '130', 'enabled': True}
<Response [201]>
realm: 3.411198
token: 0.238317
{'id': '131', 'realm': '131', 'enabled': True}
<Response [201]>
realm: 3.454651
token: 0.242926
{'id': '132', 'realm': '132', 'enabled': True}
<Response [201]>
realm: 3.553636
token: 0.26433
{'id': '133', 'realm': '133', 'enabled': True}
<Response [201]>
realm: 3.532358
token: 0.236722
{'id': '134', 'realm': '134', 'enabled': True}
<Response [201]>
realm: 3.669426
token: 0.238807
{'id': '135', 'realm': '135', 'enabled': True}
<Response [201]>
realm: 3.49426
token: 0.243782
{'id': '136', 'realm': '136', 'enabled': True}
<Response [201]>
realm: 3.599762
token: 0.244735
{'id': '137', 'realm': '137', 'enabled': True}
<Response [201]>
realm: 3.754012
token: 0.238299
{'id': '138', 'realm': '138', 'enabled': True}
<Response [201]>
realm: 3.574944
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak.py 
mo@macmini:~/repo/py/keyclaok-test/src$ python3 keycloak2.py 
start
token: 0.222778
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [409]>
token: 0.142947
{'id': '1', 'realm': '1', 'enabled': True}
<Response [409]>
realm: 0.039393
token: 0.146097
{'id': '2', 'realm': '2', 'enabled': True}
<Response [409]>
realm: 0.020888
token: 0.141896
{'id': '3', 'realm': '3', 'enabled': True}
<Response [409]>
realm: 0.036249
token: 0.145584
{'id': '4', 'realm': '4', 'enabled': True}
<Response [409]>
realm: 0.022636
token: 0.145204
{'id': '5', 'realm': '5', 'enabled': True}
<Response [409]>
realm: 0.019334
token: 0.141692
{'id': '6', 'realm': '6', 'enabled': True}
<Response [409]>
realm: 0.018172
token: 0.145631
{'id': '7', 'realm': '7', 'enabled': True}
<Response [409]>
realm: 0.020897
token: 0.14378
{'id': '8', 'realm': '8', 'enabled': True}
<Response [409]>
realm: 0.022979
token: 0.144837
{'id': '9', 'realm': '9', 'enabled': True}
<Response [409]>
realm: 0.024246
:^CTraceback (most recent call last):
  File "keycloak2.py", line 90, in <module>
    main()
  File "keycloak2.py", line 81, in main
    token = get_token()
  File "keycloak2.py", line 27, in get_token
    response = requests.request("POST", url, headers=headers, data=payload)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 668, in send
    history = [resp for resp in gen] if allow_redirects else []
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 668, in <listcomp>
    history = [resp for resp in gen] if allow_redirects else []
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 150, in resolve_redirects
    previous_fragment = urlparse(req.url).fragment
  File "/usr/lib/python3.8/urllib/parse.py", line 374, in urlparse
    scheme, netloc, url, query, fragment = splitresult
KeyboardInterrupt

mo@macmini:~/repo/py/keyclaok-test/src$ ^C
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak.py 
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak.py 
mo@macmini:~/repo/py/keyclaok-test/src$ vim keycloak2.py 
mo@macmini:~/repo/py/keyclaok-test/src$ python3 keycloak2.py 
start
token: 0.143741
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [409]>
token: 0.1411
{'id': '200', 'realm': '200', 'enabled': True}
<Response [201]>
realm: 3.637214
token: 0.249609
{'id': '201', 'realm': '201', 'enabled': True}
<Response [201]>
realm: 3.717461
token: 0.242974
{'id': '202', 'realm': '202', 'enabled': True}
<Response [201]>
realm: 3.701006
token: 0.245178
{'id': '203', 'realm': '203', 'enabled': True}
<Response [201]>
realm: 3.671764
token: 0.244048
{'id': '204', 'realm': '204', 'enabled': True}
<Response [201]>
realm: 3.60783
token: 0.244295
{'id': '205', 'realm': '205', 'enabled': True}
<Response [201]>
realm: 3.633825
token: 0.244217
{'id': '206', 'realm': '206', 'enabled': True}
<Response [201]>
realm: 3.763245
token: 0.243089
{'id': '207', 'realm': '207', 'enabled': True}
<Response [201]>
realm: 3.693215
token: 0.243713
{'id': '208', 'realm': '208', 'enabled': True}
<Response [201]>
realm: 3.700769
token: 0.239856
{'id': '209', 'realm': '209', 'enabled': True}
<Response [201]>
realm: 3.664945
token: 0.24409
{'id': '210', 'realm': '210', 'enabled': True}
<Response [201]>
realm: 3.874647
token: 0.25073
{'id': '211', 'realm': '211', 'enabled': True}
<Response [201]>
realm: 3.900613
token: 0.270019
{'id': '212', 'realm': '212', 'enabled': True}
<Response [201]>
realm: 3.84994
token: 0.254283
{'id': '213', 'realm': '213', 'enabled': True}
<Response [201]>
realm: 3.981299
token: 0.276418
{'id': '214', 'realm': '214', 'enabled': True}
<Response [201]>
realm: 3.959897
token: 0.249388
{'id': '215', 'realm': '215', 'enabled': True}
<Response [201]>
realm: 3.881663
token: 0.251617
{'id': '216', 'realm': '216', 'enabled': True}
<Response [201]>
realm: 3.810302
token: 0.253087
{'id': '217', 'realm': '217', 'enabled': True}
<Response [201]>
realm: 4.131352
token: 0.249372
{'id': '218', 'realm': '218', 'enabled': True}
<Response [201]>
realm: 3.986659
token: 0.253191
{'id': '219', 'realm': '219', 'enabled': True}
<Response [201]>
realm: 3.941298
token: 0.25886
{'id': '220', 'realm': '220', 'enabled': True}
<Response [201]>
realm: 3.99625
token: 0.251638
{'id': '221', 'realm': '221', 'enabled': True}
<Response [201]>
realm: 4.049867
token: 0.259547
{'id': '222', 'realm': '222', 'enabled': True}
<Response [201]>
realm: 3.924629
token: 0.253081
{'id': '223', 'realm': '223', 'enabled': True}
<Response [201]>
realm: 3.977462
token: 0.2548
{'id': '224', 'realm': '224', 'enabled': True}
<Response [201]>
realm: 4.190107
token: 0.257961
{'id': '225', 'realm': '225', 'enabled': True}
<Response [201]>
realm: 4.173636
token: 0.25914
{'id': '226', 'realm': '226', 'enabled': True}
<Response [201]>
realm: 4.003348
token: 0.258118
{'id': '227', 'realm': '227', 'enabled': True}
<Response [201]>
realm: 4.049147
token: 0.259985
{'id': '228', 'realm': '228', 'enabled': True}
<Response [201]>
realm: 4.121509
token: 0.256997
{'id': '229', 'realm': '229', 'enabled': True}
<Response [201]>
realm: 4.049722
token: 0.268509
{'id': '230', 'realm': '230', 'enabled': True}
<Response [201]>
realm: 4.174113
token: 0.255246
{'id': '231', 'realm': '231', 'enabled': True}
<Response [201]>
realm: 4.125595
token: 0.262102
{'id': '232', 'realm': '232', 'enabled': True}
<Response [201]>
realm: 4.21186
token: 0.253586
{'id': '233', 'realm': '233', 'enabled': True}
<Response [201]>
realm: 4.179259
token: 0.261326
{'id': '234', 'realm': '234', 'enabled': True}
<Response [201]>
realm: 4.279817
token: 0.263792
{'id': '235', 'realm': '235', 'enabled': True}
<Response [201]>
realm: 4.328897
token: 0.266819
{'id': '236', 'realm': '236', 'enabled': True}
<Response [201]>
realm: 4.160573
token: 0.262655
{'id': '237', 'realm': '237', 'enabled': True}
<Response [201]>
realm: 4.310481
token: 0.269392
{'id': '238', 'realm': '238', 'enabled': True}
<Response [201]>
realm: 4.289202
token: 0.26652
{'id': '239', 'realm': '239', 'enabled': True}
<Response [201]>
realm: 4.27492
token: 0.263983
{'id': '240', 'realm': '240', 'enabled': True}
<Response [201]>
realm: 4.261506
token: 0.265532
{'id': '241', 'realm': '241', 'enabled': True}
<Response [201]>
realm: 4.223157
token: 0.27229
{'id': '242', 'realm': '242', 'enabled': True}
<Response [201]>
realm: 4.40571
token: 0.265631
{'id': '243', 'realm': '243', 'enabled': True}
<Response [201]>
realm: 4.274021
token: 0.261222
{'id': '244', 'realm': '244', 'enabled': True}
<Response [201]>
realm: 4.390685
token: 0.267912
{'id': '245', 'realm': '245', 'enabled': True}
<Response [201]>
realm: 4.567569
token: 0.266487
{'id': '246', 'realm': '246', 'enabled': True}
<Response [201]>
realm: 4.452379
token: 0.268569
{'id': '247', 'realm': '247', 'enabled': True}
<Response [201]>
realm: 4.410104
token: 0.286703
{'id': '248', 'realm': '248', 'enabled': True}
<Response [201]>
realm: 4.455205
token: 0.265191
{'id': '249', 'realm': '249', 'enabled': True}
<Response [201]>
realm: 4.474362
token: 0.272094
{'id': '250', 'realm': '250', 'enabled': True}
<Response [201]>
realm: 4.531726
token: 0.270283
{'id': '251', 'realm': '251', 'enabled': True}
<Response [201]>
realm: 4.456795
token: 0.273152
{'id': '252', 'realm': '252', 'enabled': True}
<Response [201]>
realm: 4.520869
token: 0.276682
{'id': '253', 'realm': '253', 'enabled': True}
<Response [201]>
realm: 4.629869
token: 0.27393
{'id': '254', 'realm': '254', 'enabled': True}
<Response [201]>
realm: 4.581103
token: 0.272233
{'id': '255', 'realm': '255', 'enabled': True}
<Response [201]>
realm: 4.544132
token: 0.290059
{'id': '256', 'realm': '256', 'enabled': True}
<Response [201]>
realm: 4.552588
token: 0.272168
{'id': '257', 'realm': '257', 'enabled': True}
<Response [201]>
realm: 4.695955
token: 0.311553
{'id': '258', 'realm': '258', 'enabled': True}
<Response [201]>
realm: 4.779132
token: 0.273114
{'id': '259', 'realm': '259', 'enabled': True}
<Response [201]>
realm: 4.587192
token: 0.277535
{'id': '260', 'realm': '260', 'enabled': True}
<Response [201]>
realm: 4.757293
token: 0.277305
{'id': '261', 'realm': '261', 'enabled': True}
<Response [201]>
realm: 4.737125
token: 0.274443
{'id': '262', 'realm': '262', 'enabled': True}
<Response [201]>
realm: 4.696679
token: 0.284825
{'id': '263', 'realm': '263', 'enabled': True}
<Response [201]>
realm: 4.955505
token: 0.281986
{'id': '264', 'realm': '264', 'enabled': True}
<Response [201]>
realm: 4.890752
token: 0.276148
{'id': '265', 'realm': '265', 'enabled': True}
<Response [201]>
realm: 4.655177
token: 0.27357
{'id': '266', 'realm': '266', 'enabled': True}
<Response [201]>
realm: 4.780655
token: 0.27172
{'id': '267', 'realm': '267', 'enabled': True}
<Response [201]>
realm: 4.737184
token: 0.274385
{'id': '268', 'realm': '268', 'enabled': True}
<Response [201]>
realm: 4.818651
token: 0.279901
{'id': '269', 'realm': '269', 'enabled': True}
<Response [201]>
realm: 4.884964
token: 0.279232
{'id': '270', 'realm': '270', 'enabled': True}
<Response [201]>
realm: 4.871855
token: 0.276384
{'id': '271', 'realm': '271', 'enabled': True}
<Response [201]>
realm: 4.780634
token: 0.290466
{'id': '272', 'realm': '272', 'enabled': True}
<Response [201]>
realm: 4.727004
token: 0.285932
{'id': '273', 'realm': '273', 'enabled': True}
<Response [201]>
realm: 5.074316
token: 0.282078
{'id': '274', 'realm': '274', 'enabled': True}
<Response [201]>
realm: 4.918095
token: 0.281281
{'id': '275', 'realm': '275', 'enabled': True}
<Response [201]>
realm: 4.994439
token: 0.281607
{'id': '276', 'realm': '276', 'enabled': True}
<Response [201]>
realm: 5.237788
token: 0.286344
{'id': '277', 'realm': '277', 'enabled': True}
<Response [201]>
realm: 4.944751
token: 0.276531
{'id': '278', 'realm': '278', 'enabled': True}
<Response [201]>
realm: 4.923652
token: 0.281232
{'id': '279', 'realm': '279', 'enabled': True}
<Response [201]>
realm: 5.005495
token: 0.266698
{'id': '280', 'realm': '280', 'enabled': True}
<Response [201]>
realm: 5.077842
token: 0.281942
{'id': '281', 'realm': '281', 'enabled': True}
<Response [201]>
realm: 4.909511
token: 0.288941
{'id': '282', 'realm': '282', 'enabled': True}
<Response [201]>
realm: 4.906446
token: 0.285315
{'id': '283', 'realm': '283', 'enabled': True}
<Response [201]>
realm: 5.01504
token: 0.302354
{'id': '284', 'realm': '284', 'enabled': True}
<Response [201]>
realm: 5.185946
token: 0.289493
{'id': '285', 'realm': '285', 'enabled': True}
<Response [201]>
realm: 5.13622
token: 0.297849
{'id': '286', 'realm': '286', 'enabled': True}
<Response [201]>
realm: 5.031296
token: 0.304153
{'id': '287', 'realm': '287', 'enabled': True}
<Response [201]>
realm: 5.204706
token: 0.300122
{'id': '288', 'realm': '288', 'enabled': True}
<Response [201]>
realm: 5.151799
token: 0.289544
{'id': '289', 'realm': '289', 'enabled': True}
<Response [201]>
realm: 5.125419
token: 0.286461
{'id': '290', 'realm': '290', 'enabled': True}
<Response [201]>
realm: 5.018042
token: 0.287252
{'id': '291', 'realm': '291', 'enabled': True}
<Response [201]>
realm: 5.212995
token: 0.295303
{'id': '292', 'realm': '292', 'enabled': True}
<Response [201]>
realm: 5.364148
token: 0.294641
{'id': '293', 'realm': '293', 'enabled': True}
<Response [201]>
realm: 5.198864
token: 0.290251
{'id': '294', 'realm': '294', 'enabled': True}
<Response [201]>
realm: 5.239152
token: 0.297442
{'id': '295', 'realm': '295', 'enabled': True}
<Response [201]>
realm: 5.304197
token: 0.295261
{'id': '296', 'realm': '296', 'enabled': True}
<Response [201]>
realm: 5.429042
token: 0.299035
{'id': '297', 'realm': '297', 'enabled': True}
<Response [201]>
realm: 5.516185
token: 0.294471
{'id': '298', 'realm': '298', 'enabled': True}
<Response [201]>
realm: 5.283184
token: 0.300912
{'id': '299', 'realm': '299', 'enabled': True}
<Response [201]>
realm: 5.241898
token: 0.294408
{'id': '300', 'realm': '300', 'enabled': True}
<Response [201]>
realm: 5.643361
token: 0.296652
{'id': '301', 'realm': '301', 'enabled': True}
<Response [201]>
realm: 5.401602
token: 0.30457
{'id': '302', 'realm': '302', 'enabled': True}
<Response [201]>
realm: 5.478966
token: 0.297858
{'id': '303', 'realm': '303', 'enabled': True}
<Response [201]>
realm: 5.347367
token: 0.298649
{'id': '304', 'realm': '304', 'enabled': True}
<Response [201]>
realm: 5.322831
token: 0.304905
{'id': '305', 'realm': '305', 'enabled': True}
<Response [201]>
realm: 5.513566
token: 0.306139
{'id': '306', 'realm': '306', 'enabled': True}
<Response [201]>
realm: 5.320488
token: 0.301803
{'id': '307', 'realm': '307', 'enabled': True}
<Response [201]>
realm: 5.558048
token: 0.304909
{'id': '308', 'realm': '308', 'enabled': True}
<Response [201]>
realm: 5.464694
token: 0.29773
{'id': '309', 'realm': '309', 'enabled': True}
<Response [201]>
realm: 5.874081
token: 0.301672
{'id': '310', 'realm': '310', 'enabled': True}
<Response [201]>
realm: 5.680328
token: 0.308567
{'id': '311', 'realm': '311', 'enabled': True}
<Response [201]>
realm: 5.505718
token: 0.310866
{'id': '312', 'realm': '312', 'enabled': True}
<Response [201]>
realm: 5.589941
token: 0.30005
{'id': '313', 'realm': '313', 'enabled': True}
<Response [201]>
realm: 5.560467
token: 0.308736
{'id': '314', 'realm': '314', 'enabled': True}
<Response [201]>
realm: 5.286842
token: 0.299425
{'id': '315', 'realm': '315', 'enabled': True}
<Response [201]>
realm: 5.776937
token: 0.300361
{'id': '316', 'realm': '316', 'enabled': True}
<Response [201]>
realm: 5.75552
token: 0.296444
{'id': '317', 'realm': '317', 'enabled': True}
<Response [201]>
realm: 5.654742
token: 0.321158
{'id': '318', 'realm': '318', 'enabled': True}
<Response [201]>
realm: 5.56459
token: 0.30371
{'id': '319', 'realm': '319', 'enabled': True}
<Response [201]>
realm: 5.625675
token: 0.322298
{'id': '320', 'realm': '320', 'enabled': True}
<Response [201]>
realm: 5.970028
token: 0.308758
{'id': '321', 'realm': '321', 'enabled': True}
<Response [201]>
realm: 5.739522
token: 0.300638
{'id': '322', 'realm': '322', 'enabled': True}
<Response [201]>
realm: 6.113413
token: 0.311085
{'id': '323', 'realm': '323', 'enabled': True}
<Response [201]>
realm: 6.108337
token: 0.319135
{'id': '324', 'realm': '324', 'enabled': True}
<Response [201]>
realm: 6.040748
token: 0.362152
{'id': '325', 'realm': '325', 'enabled': True}
<Response [201]>
realm: 5.861087
token: 0.316556
{'id': '326', 'realm': '326', 'enabled': True}
<Response [201]>
realm: 5.844063
token: 0.316352
{'id': '327', 'realm': '327', 'enabled': True}
<Response [201]>
realm: 5.836035
token: 0.31115
{'id': '328', 'realm': '328', 'enabled': True}
<Response [201]>
realm: 6.01731
token: 0.314204
{'id': '329', 'realm': '329', 'enabled': True}
<Response [201]>
realm: 6.040175
token: 0.308379
{'id': '330', 'realm': '330', 'enabled': True}
<Response [201]>
realm: 5.903383
token: 0.3127
{'id': '331', 'realm': '331', 'enabled': True}
<Response [201]>
realm: 5.805086
token: 0.325428
{'id': '332', 'realm': '332', 'enabled': True}
<Response [201]>
realm: 5.958055
token: 0.315512
{'id': '333', 'realm': '333', 'enabled': True}
<Response [201]>
realm: 5.784432
token: 0.313571
{'id': '334', 'realm': '334', 'enabled': True}
<Response [201]>
realm: 5.852838
token: 0.315009
{'id': '335', 'realm': '335', 'enabled': True}
<Response [201]>
realm: 6.020628
token: 0.316994
{'id': '336', 'realm': '336', 'enabled': True}
<Response [201]>
realm: 6.009941
token: 0.313843
{'id': '337', 'realm': '337', 'enabled': True}
<Response [201]>
realm: 6.047926
token: 0.308406
{'id': '338', 'realm': '338', 'enabled': True}
<Response [201]>
realm: 5.927984
token: 0.315257
{'id': '339', 'realm': '339', 'enabled': True}
<Response [201]>
realm: 5.982129
token: 0.316878
{'id': '340', 'realm': '340', 'enabled': True}
<Response [201]>
realm: 6.141424
token: 0.321925
{'id': '341', 'realm': '341', 'enabled': True}
<Response [201]>
realm: 6.030229
token: 0.333419
{'id': '342', 'realm': '342', 'enabled': True}
<Response [201]>
realm: 6.030489
token: 0.318764
{'id': '343', 'realm': '343', 'enabled': True}
<Response [201]>
realm: 6.143625
token: 0.323243
{'id': '344', 'realm': '344', 'enabled': True}
<Response [201]>
realm: 6.037001
token: 0.324925
{'id': '345', 'realm': '345', 'enabled': True}
<Response [201]>
realm: 6.165674
token: 0.327307
{'id': '346', 'realm': '346', 'enabled': True}
<Response [201]>
realm: 6.096741
token: 0.332061
{'id': '347', 'realm': '347', 'enabled': True}
<Response [201]>
realm: 6.186308
token: 0.336674
{'id': '348', 'realm': '348', 'enabled': True}
<Response [201]>
realm: 6.075526
token: 0.323415
{'id': '349', 'realm': '349', 'enabled': True}
<Response [201]>
realm: 6.140936
token: 0.329434
{'id': '350', 'realm': '350', 'enabled': True}
<Response [201]>
realm: 6.027081
token: 0.433455
{'id': '351', 'realm': '351', 'enabled': True}
<Response [201]>
realm: 6.065102
token: 0.328947
{'id': '352', 'realm': '352', 'enabled': True}
<Response [201]>
realm: 6.389718
token: 0.324213
{'id': '353', 'realm': '353', 'enabled': True}
<Response [201]>
realm: 6.211854
token: 0.326911
{'id': '354', 'realm': '354', 'enabled': True}
<Response [201]>
realm: 6.306495
token: 0.332422
{'id': '355', 'realm': '355', 'enabled': True}
<Response [201]>
realm: 6.383212
token: 0.326731
{'id': '356', 'realm': '356', 'enabled': True}
<Response [201]>
realm: 6.433278
token: 0.34404
{'id': '357', 'realm': '357', 'enabled': True}
<Response [201]>
realm: 6.288688
token: 0.334159
{'id': '358', 'realm': '358', 'enabled': True}
<Response [201]>
realm: 6.275018
token: 0.33267
{'id': '359', 'realm': '359', 'enabled': True}
<Response [201]>
realm: 6.243854
token: 0.327322
{'id': '360', 'realm': '360', 'enabled': True}
<Response [201]>
realm: 6.31971
token: 0.332918
{'id': '361', 'realm': '361', 'enabled': True}
<Response [201]>
realm: 6.379304
token: 0.330204
{'id': '362', 'realm': '362', 'enabled': True}
<Response [201]>
realm: 6.395464
token: 0.349968
{'id': '363', 'realm': '363', 'enabled': True}
<Response [201]>
realm: 6.335642
token: 0.333337
{'id': '364', 'realm': '364', 'enabled': True}
<Response [201]>
realm: 6.46492
token: 0.332652
{'id': '365', 'realm': '365', 'enabled': True}
<Response [201]>
realm: 6.462207
token: 0.329628
{'id': '366', 'realm': '366', 'enabled': True}
<Response [201]>
realm: 6.521559
token: 0.337125
{'id': '367', 'realm': '367', 'enabled': True}
<Response [201]>
realm: 6.783614
token: 0.347283
{'id': '368', 'realm': '368', 'enabled': True}
<Response [201]>
realm: 6.595967
token: 0.330142
{'id': '369', 'realm': '369', 'enabled': True}
<Response [201]>
realm: 6.796088
token: 0.336425
{'id': '370', 'realm': '370', 'enabled': True}
<Response [201]>
realm: 6.588607
token: 0.333317
{'id': '371', 'realm': '371', 'enabled': True}
<Response [201]>
realm: 6.542835
token: 0.338099
{'id': '372', 'realm': '372', 'enabled': True}
<Response [201]>
realm: 6.512991
token: 0.33512
{'id': '373', 'realm': '373', 'enabled': True}
<Response [201]>
realm: 6.438022
token: 0.338775
{'id': '374', 'realm': '374', 'enabled': True}
<Response [201]>
realm: 6.624214
token: 0.339162
{'id': '375', 'realm': '375', 'enabled': True}
<Response [201]>
realm: 6.502574
token: 0.340556
{'id': '376', 'realm': '376', 'enabled': True}
<Response [201]>
realm: 6.784871
token: 0.346436
{'id': '377', 'realm': '377', 'enabled': True}
<Response [201]>
realm: 6.458428
token: 0.341343
{'id': '378', 'realm': '378', 'enabled': True}
<Response [201]>
realm: 6.601717
token: 0.338704
{'id': '379', 'realm': '379', 'enabled': True}
<Response [201]>
realm: 6.642705
token: 0.339049
{'id': '380', 'realm': '380', 'enabled': True}
<Response [201]>
realm: 6.603709
token: 0.344365
{'id': '381', 'realm': '381', 'enabled': True}
<Response [201]>
realm: 6.586294
token: 0.340742
{'id': '382', 'realm': '382', 'enabled': True}
<Response [201]>
realm: 6.512429
token: 0.34556
{'id': '383', 'realm': '383', 'enabled': True}
<Response [201]>
realm: 6.692235
token: 0.345834
{'id': '384', 'realm': '384', 'enabled': True}
<Response [201]>
realm: 6.591499
token: 0.348313
{'id': '385', 'realm': '385', 'enabled': True}
<Response [201]>
realm: 6.614538
token: 0.351483
{'id': '386', 'realm': '386', 'enabled': True}
<Response [201]>
realm: 6.626108
token: 0.349069
{'id': '387', 'realm': '387', 'enabled': True}
<Response [201]>
realm: 6.894564
token: 0.351258
{'id': '388', 'realm': '388', 'enabled': True}
<Response [201]>
realm: 6.819315
token: 0.342251
{'id': '389', 'realm': '389', 'enabled': True}
<Response [201]>
realm: 6.787348
token: 0.359536
{'id': '390', 'realm': '390', 'enabled': True}
<Response [201]>
realm: 6.754598
token: 0.355319
{'id': '391', 'realm': '391', 'enabled': True}
<Response [201]>
realm: 6.862518
token: 0.400506
{'id': '392', 'realm': '392', 'enabled': True}
<Response [201]>
realm: 6.830837
token: 0.34918
{'id': '393', 'realm': '393', 'enabled': True}
<Response [201]>
realm: 6.925678
token: 0.349616
{'id': '394', 'realm': '394', 'enabled': True}
<Response [201]>
realm: 7.059057
token: 0.356086
{'id': '395', 'realm': '395', 'enabled': True}
<Response [201]>
realm: 6.891974
token: 0.346711
{'id': '396', 'realm': '396', 'enabled': True}
<Response [201]>
realm: 6.871121
token: 0.348278
{'id': '397', 'realm': '397', 'enabled': True}
<Response [201]>
realm: 6.95145
token: 0.344071
{'id': '398', 'realm': '398', 'enabled': True}
<Response [201]>
realm: 6.938085
token: 0.353957
{'id': '399', 'realm': '399', 'enabled': True}
<Response [201]>
realm: 6.801567
token: 0.348444
{'id': '400', 'realm': '400', 'enabled': True}
<Response [201]>
realm: 6.916227
token: 0.362809
{'id': '401', 'realm': '401', 'enabled': True}
<Response [201]>
realm: 6.892131
token: 0.350549
{'id': '402', 'realm': '402', 'enabled': True}
<Response [201]>
realm: 6.901133
token: 0.353682
{'id': '403', 'realm': '403', 'enabled': True}
<Response [201]>
realm: 6.902926
token: 0.351099
{'id': '404', 'realm': '404', 'enabled': True}
<Response [201]>
realm: 7.208263
token: 0.351819
{'id': '405', 'realm': '405', 'enabled': True}
<Response [201]>
realm: 7.233749
token: 0.354756
{'id': '406', 'realm': '406', 'enabled': True}
<Response [201]>
realm: 7.048858
token: 0.36694
{'id': '407', 'realm': '407', 'enabled': True}
<Response [201]>
realm: 7.196639
token: 0.356441
{'id': '408', 'realm': '408', 'enabled': True}
<Response [201]>
realm: 7.202853
token: 0.357242
{'id': '409', 'realm': '409', 'enabled': True}
<Response [201]>
realm: 7.244127
token: 0.354311
{'id': '410', 'realm': '410', 'enabled': True}
<Response [201]>
realm: 7.159238
token: 0.356337
{'id': '411', 'realm': '411', 'enabled': True}
<Response [201]>
realm: 7.109218
token: 0.364932
{'id': '412', 'realm': '412', 'enabled': True}
<Response [201]>
realm: 7.282828
token: 0.361144
{'id': '413', 'realm': '413', 'enabled': True}
<Response [201]>
realm: 7.324837
token: 0.361315
{'id': '414', 'realm': '414', 'enabled': True}
<Response [201]>
realm: 7.469615
token: 0.359794
{'id': '415', 'realm': '415', 'enabled': True}
<Response [201]>
realm: 7.269219
token: 0.357556
{'id': '416', 'realm': '416', 'enabled': True}
<Response [201]>
realm: 7.326518
token: 0.360997
{'id': '417', 'realm': '417', 'enabled': True}
<Response [201]>
realm: 7.264649
token: 0.359033
{'id': '418', 'realm': '418', 'enabled': True}
<Response [201]>
realm: 7.013605
token: 0.381447
{'id': '419', 'realm': '419', 'enabled': True}
<Response [201]>
realm: 7.198438
token: 0.36423
{'id': '420', 'realm': '420', 'enabled': True}
<Response [201]>
realm: 7.290335
token: 0.367383
{'id': '421', 'realm': '421', 'enabled': True}
<Response [201]>
realm: 7.225931
token: 0.364305
{'id': '422', 'realm': '422', 'enabled': True}
<Response [201]>
realm: 7.268927
token: 0.360241
{'id': '423', 'realm': '423', 'enabled': True}
<Response [201]>
realm: 8.454578
token: 0.540065
{'id': '424', 'realm': '424', 'enabled': True}
<Response [201]>
realm: 8.040636
token: 0.395695
{'id': '425', 'realm': '425', 'enabled': True}
<Response [201]>
realm: 8.680139
token: 0.381439
{'id': '426', 'realm': '426', 'enabled': True}
<Response [201]>
realm: 8.457609
token: 0.43277
{'id': '427', 'realm': '427', 'enabled': True}
<Response [201]>
realm: 8.528031
token: 0.457422
{'id': '428', 'realm': '428', 'enabled': True}
<Response [201]>
realm: 8.531467
token: 0.580118
{'id': '429', 'realm': '429', 'enabled': True}
<Response [201]>
realm: 8.479885
token: 0.417752
{'id': '430', 'realm': '430', 'enabled': True}
<Response [201]>
realm: 8.348668
token: 0.510133
{'id': '431', 'realm': '431', 'enabled': True}
<Response [201]>
realm: 8.618841
token: 0.474179
{'id': '432', 'realm': '432', 'enabled': True}
<Response [201]>
realm: 8.268659
token: 0.3764
{'id': '433', 'realm': '433', 'enabled': True}
<Response [201]>
realm: 8.107074
token: 0.572947
{'id': '434', 'realm': '434', 'enabled': True}
<Response [201]>
realm: 8.219002
token: 0.43707
{'id': '435', 'realm': '435', 'enabled': True}
<Response [201]>
realm: 8.216852
token: 0.38309
{'id': '436', 'realm': '436', 'enabled': True}
<Response [201]>
realm: 8.353281
token: 0.419788
{'id': '437', 'realm': '437', 'enabled': True}
<Response [201]>
realm: 8.502663
token: 0.508763
{'id': '438', 'realm': '438', 'enabled': True}
<Response [201]>
realm: 8.503906
token: 0.378708
{'id': '439', 'realm': '439', 'enabled': True}
<Response [201]>
realm: 8.950033
token: 0.418525
{'id': '440', 'realm': '440', 'enabled': True}
<Response [201]>
realm: 8.575858
token: 0.435066
{'id': '441', 'realm': '441', 'enabled': True}
<Response [201]>
realm: 8.486631
token: 0.460584
{'id': '442', 'realm': '442', 'enabled': True}
<Response [201]>
realm: 8.236893
token: 0.500918
{'id': '443', 'realm': '443', 'enabled': True}
<Response [201]>
realm: 8.410887
token: 0.503824
{'id': '444', 'realm': '444', 'enabled': True}
<Response [201]>
realm: 8.253484
token: 0.3945
{'id': '445', 'realm': '445', 'enabled': True}
<Response [201]>
realm: 9.230274
token: 0.384919
{'id': '446', 'realm': '446', 'enabled': True}
<Response [201]>
realm: 8.59186
token: 0.389901
{'id': '447', 'realm': '447', 'enabled': True}
<Response [201]>
realm: 8.644823
token: 0.396836
{'id': '448', 'realm': '448', 'enabled': True}
<Response [201]>
realm: 8.786889
token: 0.442858
{'id': '449', 'realm': '449', 'enabled': True}
<Response [201]>
realm: 8.455948
token: 0.460709
{'id': '450', 'realm': '450', 'enabled': True}
<Response [201]>
realm: 8.465654
token: 0.500247
{'id': '451', 'realm': '451', 'enabled': True}
<Response [201]>
realm: 8.494134
token: 0.481027
{'id': '452', 'realm': '452', 'enabled': True}
<Response [201]>
realm: 8.701606
token: 0.425855
{'id': '453', 'realm': '453', 'enabled': True}
<Response [201]>
realm: 8.849891
token: 0.391737
{'id': '454', 'realm': '454', 'enabled': True}
<Response [201]>
realm: 8.908059
token: 0.427534
{'id': '455', 'realm': '455', 'enabled': True}
<Response [201]>
realm: 8.68569
token: 0.542899
{'id': '456', 'realm': '456', 'enabled': True}
<Response [201]>
realm: 8.986031
token: 0.504309
{'id': '457', 'realm': '457', 'enabled': True}
<Response [201]>
realm: 8.746543
token: 0.482548
{'id': '458', 'realm': '458', 'enabled': True}
<Response [201]>
realm: 8.77906
token: 0.546641
{'id': '459', 'realm': '459', 'enabled': True}
<Response [201]>
realm: 9.200303
token: 0.429993
{'id': '460', 'realm': '460', 'enabled': True}
<Response [201]>
realm: 9.016707
token: 0.514661
{'id': '461', 'realm': '461', 'enabled': True}
<Response [201]>
realm: 8.636485
token: 0.54191
{'id': '462', 'realm': '462', 'enabled': True}
<Response [201]>
realm: 8.945224
token: 0.410722
{'id': '463', 'realm': '463', 'enabled': True}
<Response [201]>
realm: 9.413351
token: 0.392706
{'id': '464', 'realm': '464', 'enabled': True}
<Response [201]>
realm: 8.847904
token: 0.458713
{'id': '465', 'realm': '465', 'enabled': True}
<Response [201]>
realm: 8.886649
token: 0.394401
{'id': '466', 'realm': '466', 'enabled': True}
<Response [201]>
realm: 8.942411
token: 0.450278
{'id': '467', 'realm': '467', 'enabled': True}
<Response [201]>
realm: 9.713887
token: 0.446166
{'id': '468', 'realm': '468', 'enabled': True}
<Response [201]>
realm: 8.974834
token: 0.642666
{'id': '469', 'realm': '469', 'enabled': True}
<Response [201]>
realm: 9.343049
token: 0.482869
{'id': '470', 'realm': '470', 'enabled': True}
<Response [201]>
realm: 9.415452
token: 0.394611
{'id': '471', 'realm': '471', 'enabled': True}
<Response [201]>
realm: 9.089369
token: 0.538638
{'id': '472', 'realm': '472', 'enabled': True}
<Response [201]>
realm: 9.19106
token: 0.38874
{'id': '473', 'realm': '473', 'enabled': True}
<Response [201]>
realm: 8.278736
token: 0.398405
{'id': '474', 'realm': '474', 'enabled': True}
<Response [201]>
realm: 8.2487
token: 0.456999
{'id': '475', 'realm': '475', 'enabled': True}
<Response [201]>
realm: 8.282983
token: 0.394507
{'id': '476', 'realm': '476', 'enabled': True}
<Response [201]>
realm: 8.580842
token: 0.391704
{'id': '477', 'realm': '477', 'enabled': True}
<Response [201]>
realm: 8.349419
token: 0.393151
{'id': '478', 'realm': '478', 'enabled': True}
<Response [201]>
realm: 8.609745
token: 0.390916
{'id': '479', 'realm': '479', 'enabled': True}
<Response [201]>
realm: 8.197255
token: 0.394618
{'id': '480', 'realm': '480', 'enabled': True}
<Response [201]>
realm: 8.242362
token: 0.401431
{'id': '481', 'realm': '481', 'enabled': True}
<Response [201]>
realm: 8.345527
token: 0.391834
{'id': '482', 'realm': '482', 'enabled': True}
<Response [201]>
realm: 8.526996
token: 0.394905
{'id': '483', 'realm': '483', 'enabled': True}
<Response [201]>
realm: 8.294101
token: 0.409551
{'id': '484', 'realm': '484', 'enabled': True}
<Response [201]>
realm: 8.413757
token: 0.396902
{'id': '485', 'realm': '485', 'enabled': True}
<Response [201]>
realm: 8.41006
token: 0.396179
{'id': '486', 'realm': '486', 'enabled': True}
<Response [201]>
realm: 8.523218
token: 0.399128
{'id': '487', 'realm': '487', 'enabled': True}
<Response [201]>
realm: 8.69224
token: 0.392123
{'id': '488', 'realm': '488', 'enabled': True}
<Response [201]>
realm: 8.322633
token: 0.403097
{'id': '489', 'realm': '489', 'enabled': True}
<Response [201]>
realm: 8.309119
token: 0.393515
{'id': '490', 'realm': '490', 'enabled': True}
<Response [201]>
realm: 8.499315
token: 0.434572
{'id': '491', 'realm': '491', 'enabled': True}
<Response [201]>
realm: 8.74936
token: 0.405702
{'id': '492', 'realm': '492', 'enabled': True}
<Response [201]>
realm: 8.310184
token: 0.399047
{'id': '493', 'realm': '493', 'enabled': True}
<Response [201]>
realm: 8.638963
token: 0.404975
{'id': '494', 'realm': '494', 'enabled': True}
<Response [201]>
realm: 8.659651
token: 0.405143
{'id': '495', 'realm': '495', 'enabled': True}
<Response [201]>
realm: 8.759633
token: 0.427091
{'id': '496', 'realm': '496', 'enabled': True}
<Response [201]>
realm: 8.517705
token: 0.407164
{'id': '497', 'realm': '497', 'enabled': True}
<Response [201]>
realm: 8.558462
token: 0.449112
{'id': '498', 'realm': '498', 'enabled': True}
<Response [201]>
realm: 8.603645
token: 0.403022
{'id': '499', 'realm': '499', 'enabled': True}
<Response [201]>
realm: 8.833854
token: 0.402132
{'id': '500', 'realm': '500', 'enabled': True}
<Response [201]>
realm: 8.686989
token: 0.401753
{'id': '501', 'realm': '501', 'enabled': True}
<Response [201]>
realm: 8.675642
token: 0.401153
{'id': '502', 'realm': '502', 'enabled': True}
<Response [201]>
realm: 8.940827
token: 0.402538
{'id': '503', 'realm': '503', 'enabled': True}
<Response [201]>
realm: 9.007267
token: 0.405941
{'id': '504', 'realm': '504', 'enabled': True}
<Response [201]>
realm: 9.568246
token: 3.17793
{'id': '505', 'realm': '505', 'enabled': True}
<Response [201]>
realm: 10.317657
token: 2.135385
{'id': '506', 'realm': '506', 'enabled': True}
<Response [201]>
realm: 10.30186
token: 1.794061
{'id': '507', 'realm': '507', 'enabled': True}
<Response [201]>
realm: 9.890701
token: 2.001916
{'id': '508', 'realm': '508', 'enabled': True}
<Response [201]>
realm: 9.898153
token: 1.743173
{'id': '509', 'realm': '509', 'enabled': True}
<Response [201]>
realm: 10.318084
token: 1.759212
{'id': '510', 'realm': '510', 'enabled': True}
<Response [201]>
realm: 10.007559
token: 2.020308
{'id': '511', 'realm': '511', 'enabled': True}
<Response [201]>
realm: 9.649527
token: 1.744326
{'id': '512', 'realm': '512', 'enabled': True}
<Response [201]>
realm: 10.054126
token: 1.348898
{'id': '513', 'realm': '513', 'enabled': True}
<Response [201]>
realm: 10.655181
token: 0.497981
{'id': '514', 'realm': '514', 'enabled': True}
<Response [201]>
realm: 10.178782
token: 0.631243
{'id': '515', 'realm': '515', 'enabled': True}
<Response [201]>
realm: 10.566336
token: 1.726203
{'id': '516', 'realm': '516', 'enabled': True}
<Response [201]>
realm: 9.991377
token: 1.452369
{'id': '517', 'realm': '517', 'enabled': True}
<Response [201]>
realm: 10.686933
token: 1.397312
{'id': '518', 'realm': '518', 'enabled': True}
<Response [201]>
realm: 9.666177
token: 1.508452
{'id': '519', 'realm': '519', 'enabled': True}
<Response [201]>
realm: 10.466554
token: 1.818888
{'id': '520', 'realm': '520', 'enabled': True}
<Response [201]>
realm: 10.297261
token: 1.77111
{'id': '521', 'realm': '521', 'enabled': True}
<Response [201]>
realm: 9.90438
token: 1.34882
{'id': '522', 'realm': '522', 'enabled': True}
<Response [201]>
realm: 10.145641
token: 1.46731
{'id': '523', 'realm': '523', 'enabled': True}
<Response [201]>
realm: 10.543235
token: 1.454467
{'id': '524', 'realm': '524', 'enabled': True}
<Response [201]>
realm: 10.313237
token: 1.685312
{'id': '525', 'realm': '525', 'enabled': True}
<Response [201]>
realm: 10.536052
token: 1.381464
{'id': '526', 'realm': '526', 'enabled': True}
<Response [201]>
realm: 10.422318
token: 1.374917
{'id': '527', 'realm': '527', 'enabled': True}
<Response [201]>
realm: 10.434585
token: 1.215018
{'id': '528', 'realm': '528', 'enabled': True}
<Response [201]>
realm: 10.423827
token: 1.024271
{'id': '529', 'realm': '529', 'enabled': True}
<Response [201]>
realm: 10.10763
token: 1.054455
{'id': '530', 'realm': '530', 'enabled': True}
<Response [201]>
realm: 10.608701
token: 1.073221
{'id': '531', 'realm': '531', 'enabled': True}
<Response [201]>
realm: 9.857442
token: 1.17259
{'id': '532', 'realm': '532', 'enabled': True}
<Response [201]>
realm: 10.462708
token: 0.938458
{'id': '533', 'realm': '533', 'enabled': True}
<Response [201]>
realm: 10.667143
token: 0.872055
{'id': '534', 'realm': '534', 'enabled': True}
<Response [201]>
realm: 10.69222
token: 0.855418
{'id': '535', 'realm': '535', 'enabled': True}
<Response [201]>
realm: 10.914
token: 0.732032
{'id': '536', 'realm': '536', 'enabled': True}
<Response [201]>
realm: 11.414336
token: 0.584045
{'id': '537', 'realm': '537', 'enabled': True}
<Response [201]>
realm: 10.872346
token: 0.693928
{'id': '538', 'realm': '538', 'enabled': True}
<Response [201]>
realm: 10.088591
token: 0.594108
{'id': '539', 'realm': '539', 'enabled': True}
<Response [201]>
realm: 10.844537
token: 0.620936
{'id': '540', 'realm': '540', 'enabled': True}
<Response [201]>
realm: 10.81705
token: 0.766482
{'id': '541', 'realm': '541', 'enabled': True}
<Response [201]>
realm: 10.552722
token: 0.646653
{'id': '542', 'realm': '542', 'enabled': True}
<Response [201]>
realm: 10.535322
token: 0.958755
{'id': '543', 'realm': '543', 'enabled': True}
<Response [201]>
realm: 10.8541
token: 0.926948
{'id': '544', 'realm': '544', 'enabled': True}
<Response [201]>
realm: 11.155576
token: 0.93329
{'id': '545', 'realm': '545', 'enabled': True}
<Response [201]>
realm: 10.372412
token: 1.2869
{'id': '546', 'realm': '546', 'enabled': True}
<Response [201]>
realm: 10.959653
token: 0.691805
{'id': '547', 'realm': '547', 'enabled': True}
<Response [201]>
realm: 10.654813
token: 0.687684
{'id': '548', 'realm': '548', 'enabled': True}
<Response [201]>
realm: 10.06824
token: 0.710133
{'id': '549', 'realm': '549', 'enabled': True}
<Response [201]>
realm: 9.678017
token: 0.729606
{'id': '550', 'realm': '550', 'enabled': True}
<Response [201]>
realm: 9.57279
token: 0.761998
{'id': '551', 'realm': '551', 'enabled': True}
<Response [201]>
realm: 9.628751
token: 0.724802
{'id': '552', 'realm': '552', 'enabled': True}
<Response [201]>
realm: 9.684671
token: 0.719069
{'id': '553', 'realm': '553', 'enabled': True}
<Response [201]>
realm: 9.430092
token: 0.794447
{'id': '554', 'realm': '554', 'enabled': True}
<Response [201]>
realm: 9.727794
token: 0.796432
{'id': '555', 'realm': '555', 'enabled': True}
<Response [201]>
realm: 9.736737
token: 2.234173
{'id': '556', 'realm': '556', 'enabled': True}
<Response [201]>
realm: 9.569302
token: 0.784893
{'id': '557', 'realm': '557', 'enabled': True}
<Response [201]>
realm: 9.748284
token: 1.74684
{'id': '558', 'realm': '558', 'enabled': True}
<Response [201]>
realm: 9.542846
token: 1.335778
{'id': '559', 'realm': '559', 'enabled': True}
<Response [201]>
realm: 9.592597
token: 1.433026
{'id': '560', 'realm': '560', 'enabled': True}
<Response [201]>
realm: 9.841435
token: 1.055966
{'id': '561', 'realm': '561', 'enabled': True}
<Response [201]>
realm: 9.680292
token: 1.231028
{'id': '562', 'realm': '562', 'enabled': True}
<Response [201]>
realm: 9.953668
token: 1.474599
{'id': '563', 'realm': '563', 'enabled': True}
<Response [201]>
realm: 9.811491
token: 1.345613
{'id': '564', 'realm': '564', 'enabled': True}
<Response [201]>
realm: 9.920712
token: 2.72782
{'id': '565', 'realm': '565', 'enabled': True}
<Response [201]>
realm: 9.906853
token: 1.203308
{'id': '566', 'realm': '566', 'enabled': True}
<Response [201]>
realm: 10.047246
token: 1.175825
{'id': '567', 'realm': '567', 'enabled': True}
<Response [201]>
realm: 9.734624
token: 1.331383
{'id': '568', 'realm': '568', 'enabled': True}
<Response [201]>
realm: 10.005605
token: 0.941484
{'id': '569', 'realm': '569', 'enabled': True}
<Response [201]>
realm: 9.6793
token: 1.268584
{'id': '570', 'realm': '570', 'enabled': True}
<Response [201]>
realm: 9.756511
token: 1.279677
{'id': '571', 'realm': '571', 'enabled': True}
<Response [201]>
realm: 11.859186
token: 2.155121
{'id': '572', 'realm': '572', 'enabled': True}
<Response [201]>
realm: 11.363978
token: 1.046127
{'id': '573', 'realm': '573', 'enabled': True}
<Response [201]>
realm: 11.37891
token: 1.477057
{'id': '574', 'realm': '574', 'enabled': True}
<Response [201]>
realm: 11.514162
token: 0.997023
{'id': '575', 'realm': '575', 'enabled': True}
<Response [201]>
realm: 11.432126
token: 1.242372
{'id': '576', 'realm': '576', 'enabled': True}
<Response [201]>
realm: 11.002999
token: 0.933698
{'id': '577', 'realm': '577', 'enabled': True}
<Response [201]>
realm: 11.283142
token: 1.119614
{'id': '578', 'realm': '578', 'enabled': True}
<Response [201]>
realm: 11.776945
token: 1.147763
{'id': '579', 'realm': '579', 'enabled': True}
<Response [201]>
realm: 10.944203
token: 1.102567
{'id': '580', 'realm': '580', 'enabled': True}
<Response [201]>
realm: 11.621928
token: 2.106862
{'id': '581', 'realm': '581', 'enabled': True}
<Response [201]>
realm: 11.96725
token: 1.193204
{'id': '582', 'realm': '582', 'enabled': True}
<Response [201]>
realm: 11.149551
token: 1.211637
{'id': '583', 'realm': '583', 'enabled': True}
<Response [201]>
realm: 11.216175
token: 1.737394
{'id': '584', 'realm': '584', 'enabled': True}
<Response [201]>
realm: 11.506576
token: 1.057978
{'id': '585', 'realm': '585', 'enabled': True}
<Response [201]>
realm: 12.206948
token: 1.40421
{'id': '586', 'realm': '586', 'enabled': True}
<Response [201]>
realm: 11.628315
token: 0.998961
{'id': '587', 'realm': '587', 'enabled': True}
<Response [201]>
realm: 11.452567
token: 1.297281
{'id': '588', 'realm': '588', 'enabled': True}
<Response [201]>
realm: 11.7353
token: 1.33602
{'id': '589', 'realm': '589', 'enabled': True}
<Response [201]>
realm: 11.201883
token: 1.147022
{'id': '590', 'realm': '590', 'enabled': True}
<Response [201]>
realm: 11.8541
token: 1.147759
{'id': '591', 'realm': '591', 'enabled': True}
<Response [201]>
realm: 12.129665
token: 1.395287
{'id': '592', 'realm': '592', 'enabled': True}
<Response [201]>
realm: 12.21622
token: 2.009649
{'id': '593', 'realm': '593', 'enabled': True}
<Response [201]>
realm: 11.662083
token: 1.338336
{'id': '594', 'realm': '594', 'enabled': True}
<Response [201]>
realm: 11.296632
token: 1.568965
{'id': '595', 'realm': '595', 'enabled': True}
<Response [201]>
realm: 11.384281
token: 1.416564
{'id': '596', 'realm': '596', 'enabled': True}
<Response [201]>
realm: 11.472241
token: 1.540712
{'id': '597', 'realm': '597', 'enabled': True}
<Response [201]>
realm: 11.896671
token: 1.476016
{'id': '598', 'realm': '598', 'enabled': True}
<Response [201]>
realm: 12.716812
token: 1.5589
{'id': '599', 'realm': '599', 'enabled': True}
<Response [201]>
realm: 13.069147
token: 1.942951
{'id': '600', 'realm': '600', 'enabled': True}
<Response [201]>
realm: 12.4973
token: 1.823189
{'id': '601', 'realm': '601', 'enabled': True}
<Response [201]>
realm: 12.169603
token: 1.496395
{'id': '602', 'realm': '602', 'enabled': True}
<Response [201]>
realm: 11.987737
token: 1.538221
{'id': '603', 'realm': '603', 'enabled': True}
<Response [201]>
realm: 12.033521
token: 1.684234
{'id': '604', 'realm': '604', 'enabled': True}
<Response [201]>
realm: 12.343705
token: 1.793223
{'id': '605', 'realm': '605', 'enabled': True}
<Response [201]>
realm: 11.914587
token: 1.44049
{'id': '606', 'realm': '606', 'enabled': True}
<Response [201]>
realm: 12.51751
token: 1.406896
{'id': '607', 'realm': '607', 'enabled': True}
<Response [201]>
realm: 11.42101
token: 1.812667
{'id': '608', 'realm': '608', 'enabled': True}
<Response [201]>
realm: 12.046447
token: 1.466982
{'id': '609', 'realm': '609', 'enabled': True}
<Response [201]>
realm: 12.163474
token: 1.464787
{'id': '610', 'realm': '610', 'enabled': True}
<Response [201]>
realm: 10.954697
token: 1.777142
{'id': '611', 'realm': '611', 'enabled': True}
<Response [201]>
realm: 10.8752
token: 1.472039
{'id': '612', 'realm': '612', 'enabled': True}
<Response [201]>
realm: 10.947157
token: 1.955635
{'id': '613', 'realm': '613', 'enabled': True}
<Response [201]>
realm: 10.79146
token: 1.398147
{'id': '614', 'realm': '614', 'enabled': True}
<Response [201]>
realm: 10.912134
token: 1.693715
{'id': '615', 'realm': '615', 'enabled': True}
<Response [201]>
realm: 10.597258
token: 1.774529
{'id': '616', 'realm': '616', 'enabled': True}
<Response [201]>
realm: 10.88782
token: 1.98895
{'id': '617', 'realm': '617', 'enabled': True}
<Response [201]>
realm: 10.677316
token: 1.452246
{'id': '618', 'realm': '618', 'enabled': True}
<Response [201]>
realm: 10.802253
token: 1.852951
{'id': '619', 'realm': '619', 'enabled': True}
<Response [201]>
realm: 10.799768
token: 2.198757
{'id': '620', 'realm': '620', 'enabled': True}
<Response [201]>
realm: 10.616642
token: 1.677346
{'id': '621', 'realm': '621', 'enabled': True}
<Response [201]>
realm: 10.842269
token: 1.677183
{'id': '622', 'realm': '622', 'enabled': True}
<Response [201]>
realm: 10.818693
token: 1.989607
{'id': '623', 'realm': '623', 'enabled': True}
<Response [201]>
realm: 10.870834
token: 1.776137
{'id': '624', 'realm': '624', 'enabled': True}
<Response [201]>
realm: 10.905797
token: 3.023336
{'id': '625', 'realm': '625', 'enabled': True}
<Response [201]>
realm: 10.6061
token: 2.128533
{'id': '626', 'realm': '626', 'enabled': True}
<Response [201]>
realm: 11.025347
token: 1.794903
{'id': '627', 'realm': '627', 'enabled': True}
<Response [201]>
realm: 10.989875
token: 2.650699
{'id': '628', 'realm': '628', 'enabled': True}
<Response [201]>
realm: 10.774787
token: 2.007442
{'id': '629', 'realm': '629', 'enabled': True}
<Response [201]>
realm: 10.973158
token: 2.039791
{'id': '630', 'realm': '630', 'enabled': True}
<Response [201]>
realm: 11.388037
token: 2.152301
{'id': '631', 'realm': '631', 'enabled': True}
<Response [201]>
realm: 12.26502
token: 1.702298
{'id': '632', 'realm': '632', 'enabled': True}
<Response [201]>
realm: 12.395377
token: 1.511846
{'id': '633', 'realm': '633', 'enabled': True}
<Response [201]>
realm: 12.468735
token: 1.605748
{'id': '634', 'realm': '634', 'enabled': True}
<Response [201]>
realm: 12.37105
token: 3.449376
{'id': '635', 'realm': '635', 'enabled': True}
<Response [201]>
realm: 12.626922
token: 1.949816
{'id': '636', 'realm': '636', 'enabled': True}
<Response [201]>
realm: 12.975252
token: 3.232399
{'id': '637', 'realm': '637', 'enabled': True}
<Response [201]>
realm: 12.916859
token: 1.641143
{'id': '638', 'realm': '638', 'enabled': True}
<Response [201]>
realm: 12.574584
token: 1.926578
{'id': '639', 'realm': '639', 'enabled': True}
<Response [201]>
realm: 13.069455
token: 2.066871
{'id': '640', 'realm': '640', 'enabled': True}
<Response [201]>
realm: 12.385221
token: 2.030572
{'id': '641', 'realm': '641', 'enabled': True}
<Response [201]>
realm: 13.115806
token: 1.914108
{'id': '642', 'realm': '642', 'enabled': True}
<Response [201]>
realm: 13.674413
token: 2.15885
{'id': '643', 'realm': '643', 'enabled': True}
<Response [201]>
realm: 13.587419
client_loop: send disconnect: Broken pipe
monoMacBook-Pro:~ mo3789530$ 
monoMacBook-Pro:~ mo3789530$ 
monoMacBook-Pro:~ mo3789530$ ssh mo@192.168.11.9
mo@192.168.11.9's password: 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-53-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage



Your Hardware Enablement Stack (HWE) is supported until April 2025.
Last login: Mon May 17 18:24:24 2021 from 192.168.11.7
mo@macmini:~$ htop
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/
c/             cs/            docker-iamges/ go/            nest/          next/          ng/            node/          py/            rust/          
mo@macmini:~$ cd repo/py/
keyclaok-test/ nmp/           policy-data/   python-tools/  sample/        
mo@macmini:~$ cd repo/py/keyclaok-test/
mo@macmini:~/repo/py/keyclaok-test$ vim src/keycloak2.py 
mo@macmini:~/repo/py/keyclaok-test$ python3  src/keycloak2.py 
start
token: 3.798092
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [409]>
token: 5.859817
{'id': '660', 'realm': '660', 'enabled': True}
<Response [409]>
realm: 0.040621
token: 4.291565
{'id': '661', 'realm': '661', 'enabled': True}
<Response [409]>
realm: 0.040205
token: 4.117817
{'id': '662', 'realm': '662', 'enabled': True}
<Response [409]>
realm: 0.041596
token: 4.967588
{'id': '663', 'realm': '663', 'enabled': True}
<Response [409]>
realm: 0.04723
token: 3.689459
{'id': '664', 'realm': '664', 'enabled': True}
<Response [409]>
realm: 0.042758
token: 5.355906
{'id': '665', 'realm': '665', 'enabled': True}
<Response [409]>
realm: 0.047553
token: 4.501395
{'id': '666', 'realm': '666', 'enabled': True}
<Response [409]>
realm: 0.041218
token: 4.916947
{'id': '667', 'realm': '667', 'enabled': True}
<Response [409]>
realm: 0.039587
token: 4.630738
{'id': '668', 'realm': '668', 'enabled': True}
<Response [409]>
realm: 0.041474
token: 3.544577
{'id': '669', 'realm': '669', 'enabled': True}
<Response [409]>
realm: 0.042681
token: 7.327343
{'id': '670', 'realm': '670', 'enabled': True}
<Response [409]>
realm: 0.046079
token: 5.853534
{'id': '671', 'realm': '671', 'enabled': True}
<Response [409]>
realm: 0.043145
token: 3.263449
{'id': '672', 'realm': '672', 'enabled': True}
<Response [409]>
realm: 0.036789
token: 5.070237
{'id': '673', 'realm': '673', 'enabled': True}
<Response [409]>
realm: 0.036084
token: 3.868214
{'id': '674', 'realm': '674', 'enabled': True}
<Response [409]>
realm: 0.055233
token: 4.025459
{'id': '675', 'realm': '675', 'enabled': True}
<Response [409]>
realm: 0.037199
token: 3.020602
{'id': '676', 'realm': '676', 'enabled': True}
<Response [409]>
realm: 0.042985
token: 5.153632
{'id': '677', 'realm': '677', 'enabled': True}
<Response [409]>
realm: 0.084251
token: 3.200178
{'id': '678', 'realm': '678', 'enabled': True}
<Response [409]>
realm: 0.037957
token: 4.182918
{'id': '679', 'realm': '679', 'enabled': True}
<Response [409]>
realm: 0.034744
token: 3.407262
{'id': '680', 'realm': '680', 'enabled': True}
<Response [409]>
realm: 0.037032
token: 3.253474
{'id': '681', 'realm': '681', 'enabled': True}
<Response [409]>
realm: 0.035199
token: 4.478704
{'id': '682', 'realm': '682', 'enabled': True}
<Response [409]>
realm: 0.043456
token: 3.291301
{'id': '683', 'realm': '683', 'enabled': True}
<Response [409]>
realm: 0.048247
token: 3.84672
{'id': '684', 'realm': '684', 'enabled': True}
<Response [409]>
realm: 0.034452
token: 3.017647
{'id': '685', 'realm': '685', 'enabled': True}
<Response [409]>
realm: 0.035309
token: 4.619524
{'id': '686', 'realm': '686', 'enabled': True}
<Response [409]>
realm: 0.048765
token: 3.374262
{'id': '687', 'realm': '687', 'enabled': True}
<Response [409]>
realm: 0.03562
token: 3.211748
{'id': '688', 'realm': '688', 'enabled': True}
<Response [409]>
realm: 0.054957
token: 2.990353
{'id': '689', 'realm': '689', 'enabled': True}
<Response [409]>
realm: 0.043402
token: 3.363978
{'id': '690', 'realm': '690', 'enabled': True}
<Response [409]>
realm: 0.039783
token: 3.672607
{'id': '691', 'realm': '691', 'enabled': True}
<Response [409]>
realm: 0.034658
token: 3.782635
{'id': '692', 'realm': '692', 'enabled': True}
<Response [409]>
realm: 0.036734
token: 3.512689
{'id': '693', 'realm': '693', 'enabled': True}
<Response [409]>
realm: 0.052685
token: 5.256295
{'id': '694', 'realm': '694', 'enabled': True}
<Response [409]>
realm: 0.05054
token: 3.331793
{'id': '695', 'realm': '695', 'enabled': True}
<Response [409]>
realm: 0.060182
token: 2.945675
{'id': '696', 'realm': '696', 'enabled': True}
<Response [409]>
realm: 0.056677
token: 3.316333
{'id': '697', 'realm': '697', 'enabled': True}
<Response [409]>
realm: 0.049264
token: 3.52289
{'id': '698', 'realm': '698', 'enabled': True}
<Response [409]>
realm: 0.034098
token: 5.44786
{'id': '699', 'realm': '699', 'enabled': True}
<Response [201]>
realm: 14.534528
token: 3.117322
{'id': '700', 'realm': '700', 'enabled': True}
<Response [201]>
realm: 14.00509
token: 4.094531
{'id': '701', 'realm': '701', 'enabled': True}
<Response [201]>
realm: 14.680897
token: 3.345537
{'id': '702', 'realm': '702', 'enabled': True}
<Response [201]>
realm: 14.108589
token: 3.028801
{'id': '703', 'realm': '703', 'enabled': True}
<Response [201]>
realm: 14.089495
token: 3.730221
{'id': '704', 'realm': '704', 'enabled': True}
<Response [201]>
realm: 13.971739
token: 3.523657
{'id': '705', 'realm': '705', 'enabled': True}
<Response [201]>
realm: 13.520849
token: 4.609685
{'id': '706', 'realm': '706', 'enabled': True}
<Response [201]>
realm: 14.554645
token: 2.948821
{'id': '707', 'realm': '707', 'enabled': True}
<Response [201]>
realm: 14.102581
token: 4.22011
{'id': '708', 'realm': '708', 'enabled': True}
<Response [201]>
realm: 14.559509

token: 2.647692
{'id': '709', 'realm': '709', 'enabled': True}
<Response [201]>
realm: 13.565319
token: 3.05656
{'id': '710', 'realm': '710', 'enabled': True}
<Response [201]>
realm: 14.359963
token: 2.715322
{'id': '711', 'realm': '711', 'enabled': True}
<Response [201]>
realm: 14.213593
token: 3.598372
{'id': '712', 'realm': '712', 'enabled': True}
<Response [201]>
realm: 14.054593
token: 2.618026
{'id': '713', 'realm': '713', 'enabled': True}
<Response [201]>
realm: 14.965035
token: 3.909395
{'id': '714', 'realm': '714', 'enabled': True}
<Response [201]>
realm: 15.132537
token: 3.706201
{'id': '715', 'realm': '715', 'enabled': True}
<Response [201]>
realm: 14.406621
token: 2.802794
{'id': '716', 'realm': '716', 'enabled': True}
<Response [201]>
realm: 14.000915
token: 2.760243
{'id': '717', 'realm': '717', 'enabled': True}
<Response [201]>
realm: 13.844198
token: 3.100072
{'id': '718', 'realm': '718', 'enabled': True}
<Response [201]>
realm: 14.559612
token: 4.00149
{'id': '719', 'realm': '719', 'enabled': True}
<Response [201]>
realm: 14.824527
token: 2.346636
{'id': '720', 'realm': '720', 'enabled': True}
<Response [201]>
realm: 15.009603
token: 2.653539
{'id': '721', 'realm': '721', 'enabled': True}
<Response [201]>
realm: 14.850943
token: 6.0593
{'id': '722', 'realm': '722', 'enabled': True}
<Response [201]>
realm: 12.518563
token: 3.602333
{'id': '723', 'realm': '723', 'enabled': True}
<Response [201]>
realm: 12.698708
token: 4.808923
{'id': '724', 'realm': '724', 'enabled': True}
<Response [201]>
realm: 12.569157
token: 3.366848
{'id': '725', 'realm': '725', 'enabled': True}
<Response [201]>
realm: 12.741854
token: 3.89243
{'id': '726', 'realm': '726', 'enabled': True}
<Response [201]>
realm: 12.768676
token: 3.179981
{'id': '727', 'realm': '727', 'enabled': True}
<Response [201]>
realm: 12.916369
token: 3.175027
{'id': '728', 'realm': '728', 'enabled': True}
<Response [201]>
realm: 12.911665
token: 3.770618
{'id': '729', 'realm': '729', 'enabled': True}
<Response [201]>
realm: 12.760601
token: 2.523714
{'id': '730', 'realm': '730', 'enabled': True}
<Response [201]>
realm: 12.783528
token: 2.997514
{'id': '731', 'realm': '731', 'enabled': True}
<Response [201]>
realm: 12.787743
token: 4.529933
{'id': '732', 'realm': '732', 'enabled': True}
<Response [201]>
realm: 12.796044
token: 3.424987
{'id': '733', 'realm': '733', 'enabled': True}
<Response [201]>
realm: 12.81487
token: 3.995943
{'id': '734', 'realm': '734', 'enabled': True}
<Response [201]>
realm: 12.822488
token: 3.806849
{'id': '735', 'realm': '735', 'enabled': True}
<Response [201]>
realm: 12.841765
token: 3.96435
{'id': '736', 'realm': '736', 'enabled': True}
<Response [201]>
realm: 12.712422
token: 3.423065
{'id': '737', 'realm': '737', 'enabled': True}
<Response [201]>
realm: 12.832741
token: 3.316663
{'id': '738', 'realm': '738', 'enabled': True}
<Response [201]>
realm: 14.323535
token: 2.625219
{'id': '739', 'realm': '739', 'enabled': True}
<Response [201]>
realm: 14.636401
token: 2.231868
{'id': '740', 'realm': '740', 'enabled': True}
<Response [201]>
realm: 15.272585
token: 3.26298
{'id': '741', 'realm': '741', 'enabled': True}
<Response [201]>
realm: 14.179411
token: 3.287117
{'id': '742', 'realm': '742', 'enabled': True}
<Response [201]>
realm: 14.729409
token: 3.098611
{'id': '743', 'realm': '743', 'enabled': True}
<Response [201]>
realm: 15.257482
token: 3.189031
{'id': '744', 'realm': '744', 'enabled': True}
<Response [201]>
realm: 15.063002
token: 3.064643
{'id': '745', 'realm': '745', 'enabled': True}
<Response [201]>
realm: 15.801264
token: 3.452293
{'id': '746', 'realm': '746', 'enabled': True}
<Response [201]>
realm: 15.458979
token: 2.859345
{'id': '747', 'realm': '747', 'enabled': True}
<Response [201]>
realm: 15.883198
token: 2.996753
{'id': '748', 'realm': '748', 'enabled': True}
<Response [201]>
realm: 14.937073
token: 2.254427
{'id': '749', 'realm': '749', 'enabled': True}
<Response [201]>
realm: 15.368494
token: 2.917505
{'id': '750', 'realm': '750', 'enabled': True}
<Response [201]>
realm: 14.903241
token: 3.075208
{'id': '751', 'realm': '751', 'enabled': True}
<Response [201]>
realm: 15.360385
token: 2.308081
{'id': '752', 'realm': '752', 'enabled': True}
<Response [201]>
realm: 15.382947
token: 3.056695
{'id': '753', 'realm': '753', 'enabled': True}
<Response [201]>
realm: 15.336835
token: 4.072254
{'id': '754', 'realm': '754', 'enabled': True}
<Response [201]>
realm: 14.845269
token: 2.781813
{'id': '755', 'realm': '755', 'enabled': True}
<Response [201]>
realm: 15.28605
token: 3.723568
{'id': '756', 'realm': '756', 'enabled': True}
<Response [201]>
realm: 15.422
token: 3.120393
{'id': '757', 'realm': '757', 'enabled': True}
<Response [201]>
realm: 14.721435
token: 3.101609
{'id': '758', 'realm': '758', 'enabled': True}
<Response [201]>
realm: 15.307711
token: 2.958136
{'id': '759', 'realm': '759', 'enabled': True}
<Response [201]>
realm: 14.809599
token: 2.769475
{'id': '760', 'realm': '760', 'enabled': True}
<Response [201]>
realm: 14.576806
token: 3.178864
{'id': '761', 'realm': '761', 'enabled': True}
<Response [201]>
realm: 15.147932
token: 3.140583
{'id': '762', 'realm': '762', 'enabled': True}
<Response [201]>
realm: 15.556284
token: 3.994144
{'id': '763', 'realm': '763', 'enabled': True}
<Response [201]>
realm: 14.901382
token: 3.453743
{'id': '764', 'realm': '764', 'enabled': True}
<Response [201]>
realm: 15.168013
token: 2.921043
{'id': '765', 'realm': '765', 'enabled': True}
<Response [201]>
realm: 15.146874
token: 2.536185
{'id': '766', 'realm': '766', 'enabled': True}
<Response [201]>
realm: 15.407924
token: 3.473622
{'id': '767', 'realm': '767', 'enabled': True}
<Response [201]>
realm: 14.257745
token: 3.864036
{'id': '768', 'realm': '768', 'enabled': True}
<Response [201]>
realm: 13.052337
token: 3.859039
{'id': '769', 'realm': '769', 'enabled': True}
<Response [201]>
realm: 13.391205
token: 4.384627
{'id': '770', 'realm': '770', 'enabled': True}
<Response [201]>
realm: 13.635887
token: 3.583032
{'id': '771', 'realm': '771', 'enabled': True}
<Response [201]>
realm: 13.060325
token: 3.790918
{'id': '772', 'realm': '772', 'enabled': True}
<Response [201]>
realm: 13.176455
token: 3.218987
{'id': '773', 'realm': '773', 'enabled': True}
<Response [201]>
realm: 13.121503
token: 3.906183
{'id': '774', 'realm': '774', 'enabled': True}
<Response [201]>
realm: 13.295394
token: 3.615637
{'id': '775', 'realm': '775', 'enabled': True}
<Response [201]>
realm: 13.279041
token: 3.074008
{'id': '776', 'realm': '776', 'enabled': True}
<Response [201]>
realm: 13.174147
token: 3.868253
{'id': '777', 'realm': '777', 'enabled': True}
<Response [201]>
realm: 13.280712
token: 3.432461
{'id': '778', 'realm': '778', 'enabled': True}
<Response [201]>
realm: 13.339149
token: 3.640902
{'id': '779', 'realm': '779', 'enabled': True}
<Response [201]>
realm: 13.410762
token: 4.505253
{'id': '780', 'realm': '780', 'enabled': True}
<Response [201]>
realm: 13.485507
token: 4.215166
{'id': '781', 'realm': '781', 'enabled': True}
<Response [201]>
realm: 13.429281
token: 4.094691
{'id': '782', 'realm': '782', 'enabled': True}
<Response [201]>
realm: 13.444105
token: 4.150989
{'id': '783', 'realm': '783', 'enabled': True}
<Response [201]>
realm: 15.245007
token: 3.710811
{'id': '784', 'realm': '784', 'enabled': True}
<Response [201]>
realm: 15.756904
token: 3.232713
{'id': '785', 'realm': '785', 'enabled': True}
<Response [201]>
realm: 15.152349
token: 3.518095
{'id': '786', 'realm': '786', 'enabled': True}
<Response [201]>
realm: 15.955298
token: 3.187092
{'id': '787', 'realm': '787', 'enabled': True}
<Response [201]>
realm: 15.508116
token: 3.334889
{'id': '788', 'realm': '788', 'enabled': True}
<Response [201]>
realm: 16.31483
token: 2.893928
{'id': '789', 'realm': '789', 'enabled': True}
<Response [201]>
realm: 15.679186
token: 2.718623
{'id': '790', 'realm': '790', 'enabled': True}
<Response [201]>
realm: 15.323701
token: 3.920538
{'id': '791', 'realm': '791', 'enabled': True}
<Response [201]>
realm: 16.718913
token: 3.391694
{'id': '792', 'realm': '792', 'enabled': True}
<Response [201]>
realm: 15.786538
token: 4.041342
{'id': '793', 'realm': '793', 'enabled': True}
<Response [201]>
realm: 16.593168
token: 2.846196
{'id': '794', 'realm': '794', 'enabled': True}
<Response [201]>
realm: 15.535611
token: 3.803855
{'id': '795', 'realm': '795', 'enabled': True}
<Response [201]>
realm: 16.746981
token: 3.01609
{'id': '796', 'realm': '796', 'enabled': True}
<Response [201]>
realm: 18.819314
token: 3.209602
{'id': '797', 'realm': '797', 'enabled': True}
<Response [201]>
realm: 16.164474
token: 3.633552
{'id': '798', 'realm': '798', 'enabled': True}
<Response [201]>
realm: 15.938046
token: 4.131371
{'id': '799', 'realm': '799', 'enabled': True}
<Response [201]>
realm: 15.282648
token: 3.389751
{'id': '800', 'realm': '800', 'enabled': True}
<Response [201]>
realm: 15.908681
token: 3.6578
{'id': '801', 'realm': '801', 'enabled': True}
<Response [201]>
realm: 16.400623
token: 3.543307
{'id': '802', 'realm': '802', 'enabled': True}
<Response [201]>
realm: 16.101595
token: 3.932074
{'id': '803', 'realm': '803', 'enabled': True}
<Response [201]>
realm: 16.527035
token: 3.592912
{'id': '804', 'realm': '804', 'enabled': True}
<Response [201]>
realm: 16.931359
token: 4.23032
{'id': '805', 'realm': '805', 'enabled': True}
<Response [201]>
realm: 16.297054
token: 3.586981
{'id': '806', 'realm': '806', 'enabled': True}
<Response [201]>
realm: 17.133271
token: 4.30357
{'id': '807', 'realm': '807', 'enabled': True}
<Response [201]>
realm: 16.454085
token: 3.583185
{'id': '808', 'realm': '808', 'enabled': True}
<Response [201]>
realm: 17.049864
token: 3.602024
{'id': '809', 'realm': '809', 'enabled': True}
<Response [201]>
realm: 17.457756
token: 3.663525
{'id': '810', 'realm': '810', 'enabled': True}
<Response [201]>
realm: 15.109357
token: 4.279962
{'id': '811', 'realm': '811', 'enabled': True}
<Response [201]>
realm: 14.281811
token: 4.392352
{'id': '812', 'realm': '812', 'enabled': True}
<Response [201]>
realm: 13.972364
token: 4.577107
{'id': '813', 'realm': '813', 'enabled': True}
<Response [201]>
realm: 14.286329
token: 4.596313
{'id': '814', 'realm': '814', 'enabled': True}
<Response [201]>
realm: 14.040437
token: 5.274193
{'id': '815', 'realm': '815', 'enabled': True}
<Response [201]>
realm: 14.290143
token: 4.901978
{'id': '816', 'realm': '816', 'enabled': True}
<Response [201]>
realm: 13.945351
token: 4.634944
{'id': '817', 'realm': '817', 'enabled': True}
<Response [201]>
realm: 13.923023
token: 4.772023
{'id': '818', 'realm': '818', 'enabled': True}
<Response [201]>
realm: 14.368577
token: 5.18496
{'id': '819', 'realm': '819', 'enabled': True}
<Response [201]>
realm: 14.235942
token: 4.690546
{'id': '820', 'realm': '820', 'enabled': True}
<Response [201]>
realm: 14.254902
token: 4.563895
{'id': '821', 'realm': '821', 'enabled': True}
<Response [201]>
realm: 14.168368
token: 4.974827
{'id': '822', 'realm': '822', 'enabled': True}
<Response [201]>
realm: 14.111321
token: 5.128345
{'id': '823', 'realm': '823', 'enabled': True}
<Response [201]>
realm: 14.07826
token: 4.577198
{'id': '824', 'realm': '824', 'enabled': True}
<Response [201]>
realm: 14.603098
token: 3.797946
{'id': '825', 'realm': '825', 'enabled': True}
<Response [201]>
realm: 16.266347
token: 4.494227
{'id': '826', 'realm': '826', 'enabled': True}
<Response [201]>
realm: 16.854116
token: 4.034271
{'id': '827', 'realm': '827', 'enabled': True}
<Response [201]>
realm: 16.625604
token: 4.117168
{'id': '828', 'realm': '828', 'enabled': True}
<Response [201]>
realm: 16.286927
token: 4.282332
{'id': '829', 'realm': '829', 'enabled': True}
<Response [201]>
realm: 16.090728
token: 4.143276
{'id': '830', 'realm': '830', 'enabled': True}
<Response [201]>
realm: 16.472902
token: 3.996338
{'id': '831', 'realm': '831', 'enabled': True}
<Response [201]>
realm: 17.636449
token: 3.769019
{'id': '832', 'realm': '832', 'enabled': True}
<Response [201]>
realm: 16.730047
token: 3.837825
{'id': '833', 'realm': '833', 'enabled': True}
<Response [201]>
realm: 17.886992
token: 3.770087
{'id': '834', 'realm': '834', 'enabled': True}
<Response [201]>
realm: 15.91674
token: 4.250639
{'id': '835', 'realm': '835', 'enabled': True}
<Response [201]>
realm: 18.135332
token: 3.820638
{'id': '836', 'realm': '836', 'enabled': True}
<Response [201]>
realm: 17.989586
token: 4.121044
{'id': '837', 'realm': '837', 'enabled': True}
<Response [201]>
realm: 17.980755
token: 3.937178
{'id': '838', 'realm': '838', 'enabled': True}
<Response [201]>
realm: 16.711582
token: 3.874872
{'id': '839', 'realm': '839', 'enabled': True}
<Response [201]>
realm: 16.584521
token: 4.304578
{'id': '840', 'realm': '840', 'enabled': True}
<Response [201]>
realm: 16.848042
token: 4.094209
{'id': '841', 'realm': '841', 'enabled': True}
<Response [201]>
realm: 16.673992
token: 3.855062
{'id': '842', 'realm': '842', 'enabled': True}
<Response [201]>
realm: 16.434437
token: 3.899574
{'id': '843', 'realm': '843', 'enabled': True}
<Response [201]>
realm: 17.893139
token: 3.825191
{'id': '844', 'realm': '844', 'enabled': True}
<Response [201]>
realm: 17.390507
token: 3.606335
{'id': '845', 'realm': '845', 'enabled': True}
<Response [201]>
realm: 17.454334
token: 4.53247
{'id': '846', 'realm': '846', 'enabled': True}
<Response [201]>
realm: 16.795971
token: 3.830104
{'id': '847', 'realm': '847', 'enabled': True}
<Response [201]>
realm: 17.405953
token: 3.647142
{'id': '848', 'realm': '848', 'enabled': True}
<Response [201]>
realm: 17.526015
token: 3.878355
{'id': '849', 'realm': '849', 'enabled': True}
<Response [201]>
realm: 18.452669
token: 3.579075
{'id': '850', 'realm': '850', 'enabled': True}
<Response [201]>
realm: 16.378485
token: 5.537763
{'id': '851', 'realm': '851', 'enabled': True}
<Response [201]>
realm: 14.887817
token: 4.26817
{'id': '852', 'realm': '852', 'enabled': True}
<Response [201]>
realm: 15.126506
token: 4.140517
{'id': '853', 'realm': '853', 'enabled': True}
<Response [201]>
realm: 14.660612
token: 3.859877
{'id': '854', 'realm': '854', 'enabled': True}
<Response [201]>
realm: 14.859606
token: 5.397847
{'id': '855', 'realm': '855', 'enabled': True}
<Response [201]>
realm: 15.042752
token: 4.349138
{'id': '856', 'realm': '856', 'enabled': True}
<Response [201]>
realm: 14.838037
token: 4.116034
{'id': '857', 'realm': '857', 'enabled': True}
<Response [201]>
realm: 14.751724
token: 5.171602
{'id': '858', 'realm': '858', 'enabled': True}
<Response [201]>
realm: 14.975659
token: 4.388153
{'id': '859', 'realm': '859', 'enabled': True}
<Response [201]>
realm: 14.392903
token: 4.815496
{'id': '860', 'realm': '860', 'enabled': True}
<Response [201]>
realm: 14.713928
token: 4.28216
{'id': '861', 'realm': '861', 'enabled': True}
<Response [201]>
realm: 15.040662
token: 5.135349
{'id': '862', 'realm': '862', 'enabled': True}
<Response [201]>
realm: 14.925941
token: 4.641423
{'id': '863', 'realm': '863', 'enabled': True}
<Response [201]>
realm: 14.771578
token: 4.368624
{'id': '864', 'realm': '864', 'enabled': True}
<Response [201]>
realm: 15.796692
token: 3.858959
{'id': '865', 'realm': '865', 'enabled': True}
<Response [201]>
realm: 16.676378
token: 4.740467
{'id': '866', 'realm': '866', 'enabled': True}
<Response [201]>
realm: 17.320022
token: 3.660767
{'id': '867', 'realm': '867', 'enabled': True}
<Response [201]>
realm: 18.279539
token: 3.573626
{'id': '868', 'realm': '868', 'enabled': True}
<Response [201]>
realm: 17.950789
token: 3.495266
{'id': '869', 'realm': '869', 'enabled': True}
<Response [201]>
realm: 17.393131
token: 3.192536
{'id': '870', 'realm': '870', 'enabled': True}
<Response [201]>
realm: 17.498725
token: 3.50122
{'id': '871', 'realm': '871', 'enabled': True}
<Response [201]>
realm: 17.369054
token: 5.406652
{'id': '872', 'realm': '872', 'enabled': True}
<Response [201]>
realm: 17.565151
token: 3.597266
{'id': '873', 'realm': '873', 'enabled': True}
<Response [201]>
realm: 18.047239
token: 4.924839
{'id': '874', 'realm': '874', 'enabled': True}
<Response [201]>
realm: 17.753055
token: 3.588975
{'id': '875', 'realm': '875', 'enabled': True}
<Response [201]>
realm: 17.081298
token: 3.762437
{'id': '876', 'realm': '876', 'enabled': True}
<Response [201]>
realm: 17.43119
token: 4.036869
{'id': '877', 'realm': '877', 'enabled': True}
<Response [201]>
realm: 17.731922
token: 3.64272
{'id': '878', 'realm': '878', 'enabled': True}
<Response [201]>
realm: 16.873888
token: 3.433891
{'id': '879', 'realm': '879', 'enabled': True}
<Response [201]>
realm: 18.117839
token: 3.65707
{'id': '880', 'realm': '880', 'enabled': True}
<Response [201]>
realm: 17.790498
token: 3.572842
{'id': '881', 'realm': '881', 'enabled': True}
<Response [201]>
realm: 17.484715
token: 7.832446
{'id': '882', 'realm': '882', 'enabled': True}
<Response [201]>
realm: 17.977274
token: 4.223075
{'id': '883', 'realm': '883', 'enabled': True}
<Response [201]>
realm: 18.914726
token: 3.77792
{'id': '884', 'realm': '884', 'enabled': True}
<Response [201]>
realm: 18.635791
token: 4.584232
{'id': '885', 'realm': '885', 'enabled': True}
<Response [201]>
realm: 19.073949
token: 4.109971
{'id': '886', 'realm': '886', 'enabled': True}
<Response [201]>
realm: 18.546814
token: 3.952401
{'id': '887', 'realm': '887', 'enabled': True}
<Response [201]>
realm: 17.610844
token: 4.117702
{'id': '888', 'realm': '888', 'enabled': True}
<Response [201]>
realm: 18.792678
token: 5.62481
{'id': '889', 'realm': '889', 'enabled': True}
<Response [201]>
realm: 17.4281
token: 4.132128
{'id': '890', 'realm': '890', 'enabled': True}
<Response [201]>
realm: 15.440332
token: 6.417383
{'id': '891', 'realm': '891', 'enabled': True}
<Response [201]>
realm: 15.3818
token: 4.817744
{'id': '892', 'realm': '892', 'enabled': True}
<Response [201]>
realm: 15.579679
token: 4.322678
{'id': '893', 'realm': '893', 'enabled': True}
<Response [201]>
realm: 15.674818
token: 6.34482
{'id': '894', 'realm': '894', 'enabled': True}
<Response [201]>
realm: 15.269505
token: 4.337142
{'id': '895', 'realm': '895', 'enabled': True}
<Response [201]>
realm: 15.522834
token: 4.426556
{'id': '896', 'realm': '896', 'enabled': True}
<Response [201]>
realm: 15.498453
token: 4.292527
{'id': '897', 'realm': '897', 'enabled': True}
<Response [201]>
realm: 15.378489
token: 4.237097
{'id': '898', 'realm': '898', 'enabled': True}
<Response [201]>
realm: 15.57831
token: 4.433327
{'id': '899', 'realm': '899', 'enabled': True}
<Response [201]>
realm: 15.522244
token: 4.404517
{'id': '900', 'realm': '900', 'enabled': True}
<Response [201]>
realm: 15.813048
token: 6.720277
{'id': '901', 'realm': '901', 'enabled': True}
<Response [201]>
realm: 15.848535
token: 4.601608
{'id': '902', 'realm': '902', 'enabled': True}
<Response [201]>
realm: 15.813366
token: 5.683347
{'id': '903', 'realm': '903', 'enabled': True}
<Response [201]>
realm: 18.21993
token: 3.756242
{'id': '904', 'realm': '904', 'enabled': True}
<Response [201]>
realm: 17.522767
token: 3.789268
{'id': '905', 'realm': '905', 'enabled': True}
<Response [201]>
realm: 17.838031
token: 3.529928
{'id': '906', 'realm': '906', 'enabled': True}
<Response [201]>
realm: 18.422946
token: 5.630305
{'id': '907', 'realm': '907', 'enabled': True}
<Response [201]>
realm: 18.295163
token: 3.752075
{'id': '908', 'realm': '908', 'enabled': True}
<Response [201]>
realm: 17.539674
token: 5.341161
{'id': '909', 'realm': '909', 'enabled': True}
<Response [201]>
realm: 19.074558
token: 4.573912
{'id': '910', 'realm': '910', 'enabled': True}
<Response [201]>
realm: 17.782045
token: 4.591351
{'id': '911', 'realm': '911', 'enabled': True}
<Response [201]>
realm: 18.473776
token: 4.39107
{'id': '912', 'realm': '912', 'enabled': True}
<Response [201]>
realm: 18.629442
token: 5.858532
{'id': '913', 'realm': '913', 'enabled': True}
<Response [201]>
realm: 18.15095
token: 4.531927
{'id': '914', 'realm': '914', 'enabled': True}
<Response [201]>
realm: 18.786179
token: 4.46702
{'id': '915', 'realm': '915', 'enabled': True}
<Response [201]>
realm: 18.306485
token: 4.424018
{'id': '916', 'realm': '916', 'enabled': True}
<Response [201]>
realm: 18.522294
token: 3.979059
{'id': '917', 'realm': '917', 'enabled': True}
<Response [201]>
realm: 18.315336
token: 4.213699
{'id': '918', 'realm': '918', 'enabled': True}
<Response [201]>
realm: 17.759378
token: 4.208917
{'id': '919', 'realm': '919', 'enabled': True}
<Response [201]>
realm: 18.710655
token: 3.762094
{'id': '920', 'realm': '920', 'enabled': True}
<Response [201]>
realm: 18.565212
token: 4.285674
{'id': '921', 'realm': '921', 'enabled': True}
<Response [201]>
realm: 18.023967
token: 3.862142
{'id': '922', 'realm': '922', 'enabled': True}
<Response [201]>
realm: 18.450666
token: 4.142852
{'id': '923', 'realm': '923', 'enabled': True}
<Response [201]>
realm: 18.466467
token: 3.850631
{'id': '924', 'realm': '924', 'enabled': True}
<Response [201]>
realm: 18.388442
token: 5.282186
{'id': '925', 'realm': '925', 'enabled': True}
<Response [201]>
realm: 19.179991
token: 4.535286
{'id': '926', 'realm': '926', 'enabled': True}
<Response [201]>
realm: 19.454348
token: 4.929831
{'id': '927', 'realm': '927', 'enabled': True}
<Response [201]>
realm: 16.601675
token: 4.754197
{'id': '928', 'realm': '928', 'enabled': True}
<Response [201]>
realm: 16.243078
token: 4.55387
{'id': '929', 'realm': '929', 'enabled': True}
<Response [201]>
realm: 16.538771
token: 5.825559
{'id': '930', 'realm': '930', 'enabled': True}
<Response [201]>
realm: 16.145353
token: 5.681416
{'id': '931', 'realm': '931', 'enabled': True}
<Response [201]>
realm: 15.823103
token: 5.072746
{'id': '932', 'realm': '932', 'enabled': True}
<Response [201]>
realm: 16.012651
token: 4.794563
{'id': '933', 'realm': '933', 'enabled': True}
<Response [201]>
realm: 15.987909
token: 4.889076
{'id': '934', 'realm': '934', 'enabled': True}
<Response [201]>
realm: 16.077604
token: 4.935509
{'id': '935', 'realm': '935', 'enabled': True}
<Response [201]>
realm: 15.984879
token: 4.794601
{'id': '936', 'realm': '936', 'enabled': True}
<Response [201]>
realm: 16.111246
token: 6.08839
{'id': '937', 'realm': '937', 'enabled': True}
<Response [201]>
realm: 15.905501
token: 5.037382
{'id': '938', 'realm': '938', 'enabled': True}
<Response [201]>
realm: 15.976325
token: 4.774796
{'id': '939', 'realm': '939', 'enabled': True}
<Response [201]>
realm: 16.152735
token: 4.272206
{'id': '940', 'realm': '940', 'enabled': True}
<Response [201]>
realm: 18.927833
token: 4.31074
{'id': '941', 'realm': '941', 'enabled': True}
<Response [201]>
realm: 19.226301
token: 4.512409
{'id': '942', 'realm': '942', 'enabled': True}
<Response [201]>
realm: 18.509615
token: 4.456207
{'id': '943', 'realm': '943', 'enabled': True}
<Response [201]>
realm: 18.954508
token: 5.439505
{'id': '944', 'realm': '944', 'enabled': True}
<Response [201]>
realm: 19.065764
token: 4.970216
{'id': '945', 'realm': '945', 'enabled': True}
<Response [201]>
realm: 18.889464
token: 4.164242
{'id': '946', 'realm': '946', 'enabled': True}
<Response [201]>
realm: 20.56389
token: 4.531058
{'id': '947', 'realm': '947', 'enabled': True}
<Response [201]>
realm: 18.941216
token: 5.239436
{'id': '948', 'realm': '948', 'enabled': True}
<Response [201]>
realm: 20.074999
token: 4.589024
{'id': '949', 'realm': '949', 'enabled': True}
<Response [201]>
realm: 19.410937
token: 5.134542
{'id': '950', 'realm': '950', 'enabled': True}
<Response [201]>
realm: 18.941678
token: 5.126891
{'id': '951', 'realm': '951', 'enabled': True}
<Response [201]>
realm: 20.010855
token: 37.183517
{'id': '952', 'realm': '952', 'enabled': True}
<Response [201]>
realm: 19.078668
token: 36.470831
{'id': '953', 'realm': '953', 'enabled': True}
<Response [201]>
realm: 20.152936
token: 38.250502
{'id': '954', 'realm': '954', 'enabled': True}
<Response [201]>
realm: 18.755958
token: 36.86772
{'id': '955', 'realm': '955', 'enabled': True}
<Response [201]>
realm: 19.794163
token: 38.53393
{'id': '956', 'realm': '956', 'enabled': True}
<Response [201]>
realm: 18.923391
token: 34.336368
{'id': '957', 'realm': '957', 'enabled': True}
<Response [201]>
realm: 16.385051
token: 34.792427
{'id': '958', 'realm': '958', 'enabled': True}
<Response [201]>
realm: 16.746013
token: 34.943041
{'id': '959', 'realm': '959', 'enabled': True}
<Response [201]>
realm: 16.531654
token: 33.902397
{'id': '960', 'realm': '960', 'enabled': True}
<Response [201]>
realm: 17.374867
token: 34.089667
{'id': '961', 'realm': '961', 'enabled': True}
<Response [201]>
realm: 16.512614
token: 36.401322
{'id': '962', 'realm': '962', 'enabled': True}
<Response [201]>
realm: 19.597215
token: 37.756105
{'id': '963', 'realm': '963', 'enabled': True}
<Response [201]>
realm: 20.289342
token: 38.244519
{'id': '964', 'realm': '964', 'enabled': True}
<Response [201]>
realm: 20.298745
token: 39.436418
{'id': '965', 'realm': '965', 'enabled': True}
<Response [201]>
realm: 19.480662
token: 39.301331
{'id': '966', 'realm': '966', 'enabled': True}
<Response [201]>
realm: 20.214413
token: 38.087333
{'id': '967', 'realm': '967', 'enabled': True}
<Response [201]>
realm: 21.072852
token: 38.778878
{'id': '968', 'realm': '968', 'enabled': True}
<Response [201]>
realm: 19.823923
token: 40.070061
{'id': '969', 'realm': '969', 'enabled': True}
<Response [201]>
realm: 19.898065
token: 36.973583
{'id': '970', 'realm': '970', 'enabled': True}
<Response [201]>
realm: 20.339711
token: 38.58147
{'id': '971', 'realm': '971', 'enabled': True}
<Response [201]>
realm: 19.483657


```






```
token: 0.179078
{'enabled': True, 'attributes': {}, 'username': 'test', 'emailVerified': ''}
<Response [409]>
token: 0.165309
{'id': '1', 'realm': '1', 'enabled': True}
<Response [201]>
realm: 1.00927
token: 0.179955
{'id': '2', 'realm': '2', 'enabled': True}
<Response [201]>
realm: 0.899007
token: 0.173158
{'id': '3', 'realm': '3', 'enabled': True}
<Response [201]>
realm: 0.829046
token: 0.170119
{'id': '4', 'realm': '4', 'enabled': True}
<Response [201]>
realm: 0.856089
token: 0.181183
{'id': '5', 'realm': '5', 'enabled': True}
<Response [201]>
realm: 0.756601
token: 0.1769
{'id': '6', 'realm': '6', 'enabled': True}
<Response [201]>
realm: 0.734686


<Response [201]>
realm: 7.592924
token: 0.374342
{'id': '420', 'realm': '420', 'enabled': True}
<Response [201]>
realm: 8.208675
token: 0.365741
{'id': '421', 'realm': '421', 'enabled': True}
<Response [201]>
realm: 7.561567
token: 0.367206
{'id': '422', 'realm': '422', 'enabled': True}
<Response [201]>
realm: 7.646455
token: 0.390144
{'id': '423', 'realm': '423', 'enabled': True}
<Response [201]>
realm: 7.867305
token: 0.375165
{'id': '424', 'realm': '424', 'enabled': True}
<Response [201]>
realm: 7.791317
token: 0.36771
{'id': '425', 'realm': '425', 'enabled': True}
<Response [201]>
realm: 7.770319
token: 0.404473
{'id': '426', 'realm': '426', 'enabled': True}
<Response [201]>
realm: 7.774744
token: 0.367959
{'id': '427', 'realm': '427', 'enabled': True}
<Response [201]>
realm: 8.152005
token: 0.375806
{'id': '428', 'realm': '428', 'enabled': True}
<Response [201]>
realm: 7.460928
token: 0.376378
{'id': '429', 'realm': '429', 'enabled': True}
<Response [201]>
realm: 7.783748
token: 0.42864

realm: 17.776313
token: 0.715529
{'id': '978', 'realm': '978', 'enabled': True}
<Response [201]>
realm: 17.286337
token: 0.696073
{'id': '979', 'realm': '979', 'enabled': True}
<Response [201]>
realm: 16.365334
token: 0.644404
{'id': '980', 'realm': '980', 'enabled': True}
<Response [201]>
realm: 17.741606
token: 0.673346
{'id': '981', 'realm': '981', 'enabled': True}
<Response [201]>
realm: 17.112094
token: 0.776113
{'id': '982', 'realm': '982', 'enabled': True}
<Response [201]>
realm: 17.640227
token: 0.696108
{'id': '983', 'realm': '983', 'enabled': True}
<Response [201]>
realm: 16.538859
token: 0.670867
{'id': '984', 'realm': '984', 'enabled': True}
<Response [201]>
realm: 17.474627
token: 0.700392
{'id': '985', 'realm': '985', 'enabled': True}
<Response [201]>
realm: 17.139526
token: 0.646639
{'id': '986', 'realm': '986', 'enabled': True}
<Response [201]>
realm: 17.80059
token: 0.678653
{'id': '987', 'realm': '987', 'enabled': True}
<Response [201]>
realm: 18.033247
token: 0.7901
{'id': '988', 'realm': '988', 'enabled': True}
<Response [201]>
realm: 17.983634
token: 0.696307
{'id': '989', 'realm': '989', 'enabled': True}
<Response [201]>
realm: 16.852428
token: 0.850779
{'id': '990', 'realm': '990', 'enabled': True}
<Response [201]>
realm: 16.894486
token: 0.656166
{'id': '991', 'realm': '991', 'enabled': True}
<Response [201]>
realm: 18.125307
token: 0.691853
{'id': '992', 'realm': '992', 'enabled': True}
<Response [201]>
realm: 16.666616
token: 0.710952
{'id': '993', 'realm': '993', 'enabled': True}
<Response [201]>
realm: 17.800268
token: 0.733047
{'id': '994', 'realm': '994', 'enabled': True}
<Response [201]>
realm: 18.196686
token: 0.714824
{'id': '995', 'realm': '995', 'enabled': True}
<Response [201]>
realm: 18.191606
token: 0.673778
{'id': '996', 'realm': '996', 'enabled': True}
<Response [201]>
realm: 17.49383
token: 0.685466
{'id': '997', 'realm': '997', 'enabled': True}
<Response [201]>
realm: 18.085102
token: 0.708717
{'id': '998', 'realm': '998', 'enabled': True}
<Response [201]>
realm: 17.573133
token: 0.685166
{'id': '999', 'realm': '999', 'enabled': True}
<Response [201]>
realm: 17.184198
token: 0.701633
{'id': '1000', 'realm': '1000', 'enabled': True}
<Response [201]>
realm: 18.123823
token: 0.761727
{'id': '1001', 'realm': '1001', 'enabled': True}
<Response [201]>
realm: 16.891039
token: 0.712441
{'id': '1002', 'realm': '1002', 'enabled': True}



```