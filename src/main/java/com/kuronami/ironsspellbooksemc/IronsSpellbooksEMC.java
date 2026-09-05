package com.kuronami.ironsspellbooksemc;

import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

/**
 * Iron's Spellbooks ProjectE EMC — a data-only integration. EMC values live in
 * {@code data/irons_spellbooks/pe_custom_conversions/} and are loaded by ProjectE
 * via datapack reload; this class only provides the {@code @Mod} entry point so
 * the project fits the standard NeoForge build / runClient pipeline.
 */
@Mod(IronsSpellbooksEMC.MODID)
public final class IronsSpellbooksEMC {
    public static final String MODID = "irons_spellbooks_emc";
    private static final Logger LOGGER = LogUtils.getLogger();

    public IronsSpellbooksEMC(IEventBus modBus) {
        LOGGER.info("Iron's Spellbooks ProjectE EMC loading. EMC via data/irons_spellbooks/pe_custom_conversions");
    }
}
