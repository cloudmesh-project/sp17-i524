rs.initiate(
          {
            _id: "repset_shard2",
            members: [
      { _id : 0, host : "129.114.33.58:27018" },
      { _id : 1, host : "129.114.111.195:27018" }
    ]
          }
        )
