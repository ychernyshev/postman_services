<template>
  <div class="about">
    <h1>Archive</h1>
    <MailString v-for="mail in mails" :key="mail.user_id" :mail_data="mail" />
  </div>
</template>

<script>
import MailString from "@/components/MailString.vue";

export default {
  name: "mail-string",
  components: {
    MailString,
  },
  data() {
    return {
      mails: [
        {
          user_id: 1,
          username: "nhumberstone0",
          email: "fbleby0@ezinearticles.com",
        },
        { user_id: 2, username: "fpariso1", email: "lduiged1@xing.com" },
        {
          user_id: 3,
          username: "machrameev2",
          email: "griedel2@aboutads.info",
        },
        { user_id: 4, username: "rscarse3", email: "gbeviss3@java.com" },
        { user_id: 5, username: "lluna4", email: "gjeannard4@time.com" },
        { user_id: 6, username: "jhowsley5", email: "srickersy5@time.com" },
        {
          user_id: 7,
          username: "tgallie6",
          email: "ncarverhill6@freewebs.com",
        },
        {
          user_id: 8,
          username: "pdagostino7",
          email: "fcriple7@hostgator.com",
        },
        { user_id: 9, username: "ehorstead8", email: "rsmitheman8@cnet.com" },
        {
          user_id: 10,
          username: "cblyth9",
          email: "llawther9@theatlantic.com",
        },
      ],
    };
  },
};
</script>
